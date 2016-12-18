#coding=utf-8
from  selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
print '设置浏览器宽480，高800显示'
driver.set_window_size(480,800);


first_url='http://www.baidu.com'
print 'new access %s' %(first_url)
driver.get(first_url);

second_url='http://news.baidu.com'
print 'new access %s' %(second_url)
driver.get(first_url);


print 'back to %s' %(first_url)
driver.back();


print 'forward to %s' %(second_url)
driver.forward();

driver.refresh();


