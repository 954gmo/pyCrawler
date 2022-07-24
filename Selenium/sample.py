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


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service('chromedriver.exe'))
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("ChromeDriver")
search_box.submit()
time.sleep(5)
driver.quit()