# -*- coding: utf-8 -*-
"""
Created on Wed May 27 02:39:49 2020

@author: ASUS
"""

from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
driver.get('https://www.amazon.com/')
driver.find_element_by_id('twotabsearchtextbox').send_keys('iphone')
driver.find_element_by_class_name('nav-input').click()
driver.quit()