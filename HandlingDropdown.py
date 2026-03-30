import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

dropdown = driver.find_element(by= By.ID, value = "dropdown")
list = Select(dropdown)
list.select_by_index(2)
time.sleep(5)

dropdown = driver.find_element(by= By.ID, value = "dropdown")
list = Select(dropdown)
list.select_by_value("1")
time.sleep(5)

dropdown = driver.find_element(by= By.ID, value = "dropdown")
list = Select(dropdown)
list.select_by_visible_text("Option 2")
time.sleep(2)


