# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:34:44 2020

@author: User
"""


from selenium import webdriver
import os

abspath = os.path.abspath(r"C:\Users\ASUS\Desktop\driver\chromedriver.exe")

browser = webdriver.Chrome(executable_path=abspath)

url = "https://www.google.com.tw/"
browser.get(url)
print(browser.title)
