from bs4 import BeautifulSoup as bs4
import requests

from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

import pdfplumber

import io

def pdf_manager(pdf_href):
    row_selected = None
    row_reference = None

    try:
        response = requests.get(pdf_href)
        response.raise_for_status()  # Raises an error if the download failed
    except requests.exceptions.InvalidSchema:
        return None

    with pdfplumber.open(io.BytesIO(response.content)) as pdf:
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
    if row_selected == None:
        return None
    else:
        return row_reference, row_selected


root_ = "https://www.federacao-triatlo.pt/ftp2015/competicoes/resultados/resultados-2025/ix-duatlo-fatima-resultados/"

driver = wd.Chrome()
driver.get(root_)

justsomelist = []

root_response = requests.get(root_)
root_soup = bs4(root_response.content, "html.parser")
i=0
iframes = root_soup.find_all('iframe', class_='pdf-viewer')
for iframe in iframes:
    i+=1
    print(i)
    # for this function we need iframe link. Extract the src
    justsomelist.append(pdf_manager(iframe.get('src')))

# objective - test pdf scrapper