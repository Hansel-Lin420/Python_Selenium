# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:45:02 2020

@author: ASUS
"""

from selenium import webdriver

driver =  webdriver.Chrome()


driver.get("http://www.baidu.com")
driver.get("http://news.baidu.com")
driver.back()
driver.forward()
driver.back()
driver.refresh()
search_text=driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()


        