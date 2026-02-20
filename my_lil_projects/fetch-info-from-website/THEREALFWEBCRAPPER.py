from bs4 import BeautifulSoup as bs4
import requests

from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import pdfplumber
import pdfkit

import io

#imo selenium is better than bs4

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options={
    "print-media-type": None,
    "enable-local-file-access": None,
}

result_list = []

def bootable_manager(table, href='0'):
    global result_list
    # the table has diferent sections, that you choose by a selector bar
    # using selenium we will choose the select that we need (the most abundant, in this case, escalões or absolutos)

    # ok, use selenium to look in table
    if href=='0':
        local = table
    else:
        local = driver.get(href)

    select_element = wdw(local, 2).until(ec.element_to_be_clickable((by.TAG_NAME, "select")))
    select = Select(select_element)
    trs = None

    no = False
    for option in select.options: 
        if 'Absolutos' in option.text: # to not repeat the same thing, make a function to do the same thing
            no = False
            trs = getTRS(local, select, option)
            break
        else:
            no = True
    
    if no:
        for option in select.options:
            if 'Escalões' in option.text:
                no = False
                trs = getTRS(local, select, option)
    """else:
        for option in select.options:
            if 'Clubes' in option.text:
                trs = getTRS(local, select, option)
            else:
                print("Failed to get info.\nError: No right selector found.")"""

    tr_selected = None
    tr_reference = None
    distance = None

    for tr in trs:
        if 'Illia Kucher' in tr.text:
            print(tr.text)
            # at this point, or we save it in a global variable, or we return it to the main variable.
            tr_selected = tr.text
        elif tr.tag_name == 'thead':
            print(tr.text)
            tr_reference = tr.text
        elif 'Corrida' in tr.text:
            print(tr.text)
            distance = tr.text
            
    if tr_selected == None:
        return None
    else:
        return tr_reference, tr_selected, distance
                
def getTRS(local, select, option):
    select.select_by_visible_text(option.text)
    # now that we found one (or multiple) of the selectos that we need, we will analise its <MainDiv>

    MainDiv = wdw(local, 10).until(ec.presence_of_element_located((by.CLASS_NAME, 'MainDiv'))) # the problem was it not finding maindiv as a coause of not haveing enough time
    trs = MainDiv.find_elements(by.TAG_NAME, 'tr')
    trs.append(MainDiv.find_element(by.TAG_NAME, 'thead'))
    return trs

    


def pdf_manager(pdf_href):
    pdf_transform = pdfkit.from_url(pdf_href, False, options=options, configuration=config)
    with pdfplumber.open(io.BytesIO(pdf_transform)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            rows = text.splitlines()
            for row in rows:
                if "Illia Kucher" in row:
                    print(row)
                    row_selected = row
                elif "Nome" in row:
                    print(row)
                    row_reference = row
    return row_reference, row_selected


driver = wd.Firefox()
"""
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options={
    "print-media-type": None,
    "enable-local-file-access": None,
}
"""
# get the link
print("Triathlon get results python script.")
root_ = "https://www.federacao-triatlo.pt/ftp2015/competicoes/resultados/resultados-2025/" #input("Link: ")

# analise root with bs4
root_response = requests.get(root_)
root_soup = bs4(root_response.content, "html.parser")

tabs = root_soup.find_all("div", class_="results-list__item")

# for each tab we will see which registation case it is and then do the thing for specific case
for tab in tabs:
    tab_name = tab.text
    tab_href = tab.find('a').get('href')
    
    # access soup to determine the case
    tab_response = requests.get(tab_href)
    tab_soup = bs4(tab_response.content, "html.parser")

    # now we need to find key elements to see which case of the registation do we have
    # . ftp-folder + bootstrap table (needs navigation in divisions "")
    # . ftp-folder + pdf

    # . bootstrap table (needs navigation in divisions "")

    # . external site + bootstrap table (needs navigation in divisions)
    CASE = 0
    SPECIAL_CASE = 0

    # now that everyting is opened, we will look for diferent elements

    if tab_soup.find('div', class_='RRPublish'):
        print("Found bootstrap table")
        CASE = 1
    if tab_soup.find('iframe', class_='pdf-viewer'):
        print("Found iframe pdf")
        CASE = 2
    if tab_soup.find('div', class_='ftp-folder'):
        print('found ftp-folders')

    ftp_folder = tab_soup.find_all('div', class_='ftp-folder')

    match CASE:
        case 1:
            """if ftp_folder:
                # open every ftp_folder using selenium
                # i dont know if I really need to open ftp folders?
                # i do catually, because i need to click the table with selenium...
                driver.get(tab_href)
                ftp_folders_sele = driver.find_elements(by.CLASS_NAME, "ftp-folder")

                for ff in ftp_folders_sele:
                    click_btn = wdw(ff, 2).until(ec.element_to_be_clickable((by.CLASS_NAME, "ftp-folder")))
                    click_btn.click()
                    print(i+1)
                    table = ff.find_element(by.CLASS_NAME, 'RRPublish')
                    # for this function we need: table soup,or maybe do everything using selenium???
                    bootable_manager(table) # bootstrap table manager
            else:
                table = tab_soup.find('div', class_='RRPublish')
                # here we need table and tab_link
                bootable_manager(table, tab_href)
            """
            driver.get(tab_href)
            ftp_folders_selenium = driver.find_elements(by.CLASS_NAME, "ftp-folder")

            if ftp_folders_selenium:
                for ff in ftp_folders_selenium:
                    ff.click()
                    table = ff.find_element(by.CLASS_NAME, 'RRPublish')
                    justsomelist = bootable_manager(table)
                    result_list.append(f"{justsomelist[1]}\n{justsomelist[2]}") # now show the distance and navigation bar in the table
            else:
                table = driver.find_element(by.CLASS_NAME, 'RRPublish')
                justsomelist = bootable_manager(table)
                result_list.append(f"{justsomelist[1]}\n{justsomelist[2]}")
        case 2:
            i=0
            iframes = tab_soup.find_all('iframe', class_='pdf-viewer')
            for iframe in iframes:
                i+=1
                print(i)
                # for this function we need iframe link. Extract the src
                pdf_manager(iframe.get('src'))
    
        

driver.quit()