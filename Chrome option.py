import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#open chrome is maximized mode
#chrom_option = webdriver.ChromeOptions()
#chrom_option.add_argument("--start-maximized")
#service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj, options=chrom_option)
#driver.get("https://vinothqaacademy.com/iframe/")
#time.sleep(5)

#open headless browser
chrom_option = webdriver.ChromeOptions()
chrom_option.add_argument("--headless")
service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj, options=chrom_option)
driver.get("https://vinothqaacademy.com/iframe/")
print("Headless mode execution completed successfully")