from bs4 import BeautifulSoup as bs4
import requests
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

driver = wd.Firefox()


print("Triathlon get results python script.")
pdf_href = input("Link: ")


driver.get(pdf_href)
wdw(driver, 3).until(ec.presence_of_all_elements_located((by.TAG_NAME, "span")))

pdf_soup = bs4(driver.page_source, "html.parser")

pdf_pages = pdf_soup.find_all('div', class_='page')

i=0
for pdf_page in pdf_pages:
    rows = str(pdf_page).split('<br')
    r=0
    for row in rows:
        r+=1
        if "Masculino" in row:
            print(f"\n{row}")
    print(r)

driver.quit()

# try pdf reader modulew