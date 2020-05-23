# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:19:13 2020

@author: ASUS
"""

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
time.sleep(2)
driver.get("https://www.google.com/")
time.sleep(2)
search_input = driver.find_element_by_name("q")
search_input.send_keys('asia university')
time.sleep(2)
start_search_btn = driver.find_element_by_name("btnK")
start_search_btn.click()

time.sleep(2)
htmltext = driver.page_source
time.sleep(2)
print(htmltext)
driver.close()