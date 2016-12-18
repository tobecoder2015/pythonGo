#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element("kw").send_keys(Keys.BACK_SPACE)
driver.find_element("kw").send_keys(Keys.CONTROL,'a');
driver.find_element("su").send_keys(Keys.ENTER)

