#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("http://www.163.com")
title=driver.title
print title

driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")

driver.find_element("pwdInput").clear()
driver.find_element("pwdInput").send_keys("passeord")

driver.find_element("loginBtn").click()

time.sleep(5)

