# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:34:44 2020

@author: User
"""


from selenium import webdriver
import os

browser = webdriver.Chrome('./chromedriver')

url = "https://www.google.com.tw/"
browser.get(url)
print(browser.title)
