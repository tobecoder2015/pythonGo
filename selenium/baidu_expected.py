#coding=utf-8
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from time import sleep ,ctime
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
title=driver.title
print title

print(ctime())
for i in range(10):
    try:
        e1=driver.find_elements_by_id('kw22')
        if e1.is_displayed():
            break
        else:
            sleep(1)
    except: pass
print 'time out'
driver.close();
print ctime()


element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'kw')))
element.send_keys('selenium')

