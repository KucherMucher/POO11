# TESTING FOR v0.1

from bs4 import BeautifulSoup as bs4
import requests

from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

driver = wd.Chrome()
tab_href = "https://www.federacao-triatlo.pt/ftp2015/competicoes/resultados/resultados-2025/iv-triatlo-sao-martinho-porto-resultados/"
tab_response = requests.get(tab_href)
tab_soup = bs4(tab_response.content, "html.parser")

# now we need to find key elements to see which case of the registation do we have
# . ftp-folder + bootstrap table (needs navigation in divisions "")
# . ftp-folder + pdf

# . bootstrap table (needs navigation in divisions "")

# . external site + bootstrap table (needs navigation in divisions)
CASE = 0
SPECIAL_CASE = 0

# now that everyting is opened, we will look if there are tables or iframe pdfs

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
        if ftp_folder:
            # open every ftp_folder using selenium
            # i dont know if I really need to open ftp folders?
            # i do catually, because i need to click the table with selenium...
            driver.get(tab_href)

            for i in range(0, len(ftp_folder)):
                click_btn = wdw(driver, 2).until(ec.element_to_be_clickable((by.CLASS_NAME, "ftp-folder")))
                click_btn.click()
                print(i+1)
    case 2:
        i=0
        for iframe in tab_soup.find_all('iframe', class_='pdf-viewer'):
            i+=1
            print(i)
driver.quit()

#TESTING - WORKS