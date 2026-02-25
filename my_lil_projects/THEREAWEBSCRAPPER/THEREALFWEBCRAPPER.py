from bs4 import BeautifulSoup as bs4
import requests

from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

import pdfplumber
import io

from btmanager import bootable_manager
from pdfmanager import pdf_manager

#imo selenium is better than bs4


result_list = []

driver = wd.Chrome()

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
    
    print(tab_name) #debug

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

    # !!!- later rework this to use selenium as bs4 is now useless -!!!
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
            # open every ftp_folder using selenium
                # i dont know if I really need to open ftp folders?
                    # i do catually, because i need to click the table with selenium...
            driver.get(tab_href)
            ftp_folders_selenium = driver.find_elements(by.CLASS_NAME, "ftp-folder")

            if ftp_folders_selenium:
                for ff in ftp_folders_selenium:
                    ff.click()
                    
                    table = ff.find_element(by.CLASS_NAME, 'RRPublish')
                    # for this function we need: table soup,or maybe do everything using selenium???
                    try:
                        justsomelist = bootable_manager(table, driver) # bootstrap table manager
                    except Exception:
                        print(f"Error: ftp-folder didnt load (maybe). This will just go to the another folder. Tab name: [{tab_name}]") #resolve this issue.
                        continue
                    if justsomelist == None:
                        continue
                    else:
                        result_list.append(f"{justsomelist[0]}\n{justsomelist[1]}\n") # now show the distance and navigation bar in the table
            else:
                table = driver.find_element(by.CLASS_NAME, 'RRPublish')
                justsomelist = bootable_manager(table, driver)
                if justsomelist == None:
                    continue
                else:
                    result_list.append(f"{justsomelist[0]}\n{justsomelist[1]}\n")
        case 2:
            i=0
            # get iframes, btw cool thing
            iframes = tab_soup.find_all('iframe', class_='pdf-viewer')
            for iframe in iframes:
                """i+=1
                print(i)"""
                pdf_href = iframe.get('data-pdf-url')
                # for this function we need iframe link. Extract the url
                justsomelist = pdf_manager(pdf_href)
                if justsomelist == None:
                    continue
                else:
                    result_list.append(f"{justsomelist[0]}\n{justsomelist[1]}\n")
    
        

driver.quit()



"""
current problem: table not loading properly, maindiv isnt found and is used an None in getTRS - affected competitions [Amora, São martinho, Casconha]
why? : maybe connection problems? bad internet? something s wrong with the website?
resolving steps:
    (optional) organize functions between modules ✓
    Idea 1. Make so that it will try to scan using select three times. (change bootable_manager, maybe getTRS and main script)
        How:
            . Reload the page
            . Use diferent selects
            . Reset Select to its original position
    Idea 2. theres a star-like button in the table, we can use that to reload the table (by clicking 2 times) - <button class="btnFavorites" title="Mostrar apenas favoritos">&nbsp;</button>

other problems: 
    . Some competitions have me in there as results but it didnt show the results (external site problem?) - make maybe code for particular cases? [Xterra, Triatlo de Oeiras, Mação]
    . 
"""