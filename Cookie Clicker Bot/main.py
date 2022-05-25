from selenium import webdriver
from selenium.webdriver.common.by import By
import time

upgrades_time = time.time() + 10

element = []
a = []

def check_upgrades(money, list, driver):
    if list[7] < money:
        a = driver.find_element(by=By.ID ,value='//*[@id="buyTime machine"]')
        a.click()
    elif list[6] < money:
        a = driver.find_element(by=By.ID, value='//*[@id="buyPortal"]')
        a.click()
    elif list[5] < money:
        a = driver.find_element(by=By.ID, value='//*[@id="buyAlchemy lab"]')
        a.click()
    elif list[4] < money:
        a = driver.find_element(by=By.ID, value='//*[@id="buyShipment"]')
        a.click()
    elif list[3] < money:
        a = driver.find_element(by=By.ID, value='//*[@id="buyMine"]')
        a.click()
    elif list[2] < money:
        a = driver.find_element(by=By.ID, value='//*[@id="buyFactory"]')
        a.click()
    elif list[1] < money:
        a = driver.find_element(by=By.XPATH, value='//*[@id="buyGrandma"]')
        a.click()
    elif list[0] < money:
        a = driver.find_element_by_xpath('//*[@id="buyCursor"]')
        a.click()

def formatted_upgrade_buttons(element):
    for i in element:
        p = i.split()
        for l in p:
            if "," in l:
                l = l.replace(",", "")
            try:
                a.append(int(l))
            except ValueError:
                pass
        return a

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

list_ = driver.find_elements(by=By.CSS_SELECTOR, value='#store')
for i in list_:
    element.append(i.text)
upgrades_list = formatted_upgrade_buttons(element)
upgrades_list.remove(5)

clicker_1 = driver.find_element(by=By.XPATH, value='//*[@id="cookie"]')

while True:
    money = int(driver.find_element(by=By.ID, value='money').text)
    clicker_1.click()
    if time.time() > upgrades_time:
        check_upgrades(money, upgrades_list, driver)
