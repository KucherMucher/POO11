from bs4 import BeautifulSoup as bs4
import requests
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pdfplumber
import io
import pdfkit

driver = wd.Firefox()
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
options={
    "print-media-type": None,
    "enable-local-file-access": None,
}

print("Triathlon get results python script.")
root_page = input("Link: ")

response = requests.get(root_page)
soup = bs4(response.content, "html.parser")

pages = soup.find_all("div", class_="results-list__item")

for wpage in pages:
    link = wpage.find('a')
    href = link.get("href")

    pdf_transform = pdfkit.from_url(href, False, options=options, configuration=config)

    gotit=False
    with pdfplumber.open(io.BytesIO(pdf_transform)) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            rows = text.splitlines()
            gotit=False
            for row in rows:
                if "Nome" in row and not gotit:
                    print(row)
                    gotit = True
                if "Illia Kucher" in row:
                    print(row)

        

#driver.quit()

