# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:08:10 2020

@author: ASUS
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

elements=driver.find_elements_by_tag_name('a')
for element in elements:    
    if '视频' in element.text:
        element.click()
