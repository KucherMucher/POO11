from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec


select_option_filter = ["Absolutos", "Escalões", "Clubes", "Individual", "Estafetas"]

def bootable_manager(table, driver, href='0'):
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

    breakyeah = False
    try:
        for filter in select_option_filter:
            #print(filter) # debug
            for option in select.options:
                if filter in option.text:
                    trs = getTRS(local, select, option)
                    breakyeah = True
                    break
            if breakyeah:
                break
    except Exception:
        print("Failed to get info.\nError: No right selector found.")

    tr_selected = None
    tr_reference = None
    distance = None

    for tr in trs:
        if 'Illia Kucher' in tr.text:
            print(tr.text)
            # at this point, or we save it in a global variable, or we return it to the main variable.
            tr_selected = tr.text
        elif tr.tag_name == 'thead':
            #print(tr.text)
            tr_reference = tr.text
        elif 'Corrida' in tr.text:
            #print(tr.text)
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