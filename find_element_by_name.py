# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 03:10:51 2020

@author: ASUS
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com.tw/')
driver.find_element_by_name('q').send_keys('asia university')
time.sleep(2)
driver.find_element_by_name('btnK').click()
time.sleep(2)

