import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://www.thetesttribe.com/blog/javascriptexecutor-in-selenium/")
time.sleep(2)
driver.get_screenshot_as_file("webpage.png")
time.sleep(2)
print("Screenshot taken successfully")
