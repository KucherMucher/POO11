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

    for tr in trs:
        if 'Illia Kucher' in tr.text:
            print(tr.text)
                
def getTRS(local, select, option):
    select.select_by_visible_text(option.text)
    # now that we found one (or multiple) of the selectos that we need, we will analise its <MainDiv>

    MainDiv = wdw(local, 10).until(ec.presence_of_element_located((by.CLASS_NAME, 'MainDiv'))) # the problem was it not finding maindiv as a coause of not haveing enough time
    trs = MainDiv.find_elements(by.TAG_NAME, 'tr')
    return trs


root_ = "https://www.federacao-triatlo.pt/ftp2015/competicoes/resultados/resultados-2025/iv-triatlo-sao-martinho-porto-resultados/"

driver = wd.Chrome()
driver.get(root_)

ftp_folders_selenium = driver.find_elements(by.CLASS_NAME, "ftp-folder")

if ftp_folders_selenium:
    for ff in ftp_folders_selenium:
        ff.click()
        table = wdw(ff, 10).until(ec.presence_of_element_located((by.CLASS_NAME, 'RRPublish')))
        bootable_manager(table)
else:
    table = driver.find_element(by.CLASS_NAME, 'RRPublish')
    bootable_manager(table)

# objective - test compatability with ftp-folders
# TESTING COMPLETE
# made more select options.
# moved one part of the function into anothger function
# 
