# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.kayak.com/stays')
# driver.get('https://www.kayak.com/hotels/Miami/2022-07-05/2022-07-06/2adults?sort=rank_a')
ele_dest_city = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div/div/div/div/div[1]/div[1]/div/div/input')
ele_search_xpath = '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section/div/div/div/div/div/div/div[2]/button'
dest_city = "Miami"
ele_dest_city.send_keys(dest_city)
time.sleep(1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ele_search_xpath))).click()
WebDriverWait(driver, 10).until(EC.title_contains(dest_city))
time.sleep(10)
htm_const = driver.page_source
with open('res.html', 'w', encoding='utf-8') as f:
    f.write(htm_const)
print(htm_const)
soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
print(soup)
infos = soup.find_all('a', class_='FLpo-big-name')

for info in infos:
    print(info.get_text())
time.sleep(60)

