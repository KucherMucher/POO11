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
import pdfkit

import io


config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options={
    "print-media-type": None,
    "enable-local-file-access": None,
}


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


root_ = "https://www.federacao-triatlo.pt/ftp2015/competicoes/resultados/resultados-2025/ix-duatlo-fatima-resultados/"

driver = wd.Chrome()
driver.get(root_)

iframes = driver.find_elements(by.TAG_NAME, "iframe")

for iframe in iframes:
    # for this function we need iframe link. Extract the src
    pdf_manager(iframe.get_attribute('src'))

# objective - test pdf scrapper