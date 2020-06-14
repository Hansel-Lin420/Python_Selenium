# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:15:07 2020

@author: ASUS
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("http://www.baidu.cn")
size = driver.find_element_by_id("kw").size
print(size)

text = driver.find_element_by_id("s-bottom-layer-right").text
print(text)

attribute=driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

result = driver.find_element_by_id("kw").is_displayed()
print(result)

above = driver.find_element_by_link_text("更多")

ActionChains(driver).move_to_element(above).perform

