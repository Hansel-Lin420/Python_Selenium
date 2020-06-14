# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:46:51 2020

@author: ASUS
"""

from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('https://www.google.com')
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('Welldone')
driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input').send_keys('Welldone\n')
