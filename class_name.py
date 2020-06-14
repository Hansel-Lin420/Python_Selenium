# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:18:28 2020

@author: ASUS
"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

driver.find_element_by_class_name('lnk-movie').click()