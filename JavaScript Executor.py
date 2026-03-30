import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://www.thetesttribe.com/blog/javascriptexecutor-in-selenium/")
time.sleep(2)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
