# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import os.path
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def sample():
    BASE_DIR = Path(__file__).resolve().parent
    driver = webdriver.Chrome(service=Service('chromedriver.exe'))
    driver.get(f"file://{os.path.join(BASE_DIR, 'login.html')}")
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.XPATH, ".//*[@id='login_form']/input[2]")
    login_btn = driver.find_element(By.XPATH, ".//input[@type='submit']")
    select = Select(driver.find_element(By.XPATH, '//form/select'))
    time.sleep(3)
    select.select_by_value("email")
    time.sleep(3)
    select.select_by_visible_text("Phone")
    time.sleep(2)
    select.select_by_index(2)

    username.send_keys('gmo')
    password.send_keys('gmo')
    time.sleep(3)
    login_btn.click()
    time.sleep(3)
    username = driver.find_element(By.NAME, 'username')
    password = driver.find_element(By.NAME, 'password')

    username.send_keys("waht")
    password.send_keys("hasejlktj")
    time.sleep(3)
    username.clear()
    password.clear()
    time.sleep(3)

    # element = driver.find_element(By.NAME, 'source')
    # target = driver.find_element(By.NAME, "target")
    #
    # from selenium.webdriver import ActionChains
    # action_chains = ActionChains(driver)
    # action_chains.drag_and_drop(element, target).perform()

    driver.quit()


if __name__ == "__main__":
    sample()
