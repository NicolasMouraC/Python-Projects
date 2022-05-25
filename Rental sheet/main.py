import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

address = []
prices = []
links = []

driver = webdriver.Chrome()

request_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79',
                   'Accept-Language': 'en-US,en;q=0.9'}

response = requests.get(url='https://www.zillow.com/texas-city-tx/rentals/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"usersSearchTerm"%3A"Texas%20City%2C%20TX"%2C"mapBounds"%3A%7B"west"%3A-95.05974520458985%2C"east"%3A-94.86233462109375%2C"south"%3A29.3003471500901%2C"north"%3A29.45681324811323%7D%2C"regionSelection"%3A%5B%7B"regionId"%3A47966%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"fsba"%3A%7B"value"%3Afalse%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"fr"%3A%7B"value"%3Atrue%7D%2C"ah"%3A%7B"value"%3Atrue%7D%7D%2C"isListVisible"%3Atrue%2C"mapZoom"%3A12%7D', headers=request_headers)
html = response.text

soup = BeautifulSoup(html, 'lxml')
ul = soup.select('#grid-search-results > ul > li')
for li in ul:
    temp = []

    temp.append(li.find_next('script').text)
    json_dict = json.loads(temp[0])

    try:
        address.append(json_dict['name'])
        prices.append(json_dict['floorSize']['value'])
        links.append((json_dict['url']))
    except KeyError:
        pass

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdA8CUUH1-cEt7KuLgP2QPBbhQDFJyJBrUO_Ki_XB6NKZ9MLw/viewform?usp=sf_link')
for item in range(len(address)):
    address_driver = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_driver = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_driver = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    sleep(5)
    address_driver.send_keys(address[item])
    price_driver.send_keys(prices[item])
    link_driver.send_keys(links[item])
    button.click()
    sleep(3)
    another_answer = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_answer.click()
    another_answer = driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

