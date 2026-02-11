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

def bootable_manager(table, href='0'):
    # the table has diferent sections, that you choose by a selector bar
    # using selenium we will choose the select that we need (the most abundant, in this case, escalões or absolutos)

    # ok, use selenium to look in table
    if href=='0':
        local = table
    else:
        local = driver.get(href)

    select_element = wdw(local, 2).until(ec.element_to_be_clickable((by.TAG_NAME, "select")))
    
    
    select = Select(select_element)
    for option in select.options:
        if 'Absolutos' in option.text:
            select.select_by_visible_text(option.text)

            # now that we found one (or multiple) of the selectos that we need, we will analise its <MainDiv>
            # another way of geting the option, getting the value of the option "Absolutos" and modify the link to paste there the value of this option

            MainDiv = wdw(local, 10).until(ec.presence_of_element_located((by.CLASS_NAME, 'MainDiv')))
            # the problem was it not finding maindiv as a cause of not haveing enough time

            trs = MainDiv.find_elements(by.TAG_NAME, 'tr')

            for tr in trs:
                if 'Illia Kucher' in tr.text:
                    print("Illia Kucher found")

    


def pdf_manager(pdf_href):
    return 0


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
                    bootable_manager(table)
            else:
                table = driver.find_element(by.CLASS_NAME, 'RRPublish')
                bootable_manager(table)
        case 2:
            i=0
            iframes = tab_soup.find_all('iframe', class_='pdf-viewer')
            for iframe in iframes:
                i+=1
                print(i)
                # for this function we need iframe link. Extract the src
                pdf_manager(iframe.get('src'))
    
        

driver.quit()