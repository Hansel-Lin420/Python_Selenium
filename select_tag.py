# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:08:42 2020

@author: ASUS
"""
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.timeanddate.com/')
monthElement = driver.find_element_by_id('month')
month = Select(monthElement)
month.select_by_visible_text('December')

countriesElement = driver.find_element_by_id('country')
country = Select(countriesElement)
country.select_by_visible_text('South Korea')

driver.find_element_by_xpath('//*[@id="cf"]/div[4]/input').click()
