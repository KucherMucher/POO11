from bs4 import BeautifulSoup as bs4
import requests
from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import pdfplumber
import io

driver = wd.Firefox()


print("Triathlon get results python script.")
root_page = input("Link: ")

response = requests.get(root_page)
soup = bs4(response.content, "html.parser")

pages = soup.find_all("div", class_="results-list__item")

for wpage in pages:
    link = wpage.find('a')
    href = link.get("href")

    try:
        driver.get(href)

        click_btn = wdw(driver, 2).until(ec.element_to_be_clickable((by.CLASS_NAME, "ListControlPDF")))
        click_btn.click()

        pdf_link = wdw(driver, 2).until(ec.presence_of_element_located((by.CSS_SELECTOR, 'a[href*=".pdf"]')))
        pdf_href = pdf_link.get_attribute("href")

    except TimeoutException:
        pdf_href = href

    pdf_response = requests.get(pdf_href)
    
    with pdfplumber.open(io.BytesIO(pdf_response.content)) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            rows = text.split("\n")
            gotit=False
            for row in rows:
                if "Nome" in row and not gotit:
                    print(row)
                    gotit = True
                if "Illia Kucher" in row:
                    print(row)

        

driver.quit()