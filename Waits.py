import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://the-internet.herokuapp.com/")
#Implicit Wait
#driver.implicitly_wait(10)
#slow_element = driver.find_element(by = By.LINK_TEXT, value = "Slow Resources")
#slow_element.click()
#content = driver.find_element(by = By.XPATH, value = "//h3[text()='Slow Resources']")
#print (content.text)

#Explicit Wait
driver.implicitly_wait(10)
slow_element = driver.find_element(by = By.LINK_TEXT, value = "Slow Resources")
slow_element.click()
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.visibility_of(driver.find_element(by = By.XPATH, value = "//p[contains (text() ,  'third-party')]")))
content_text = driver.find_element(by = By.XPATH, value = "//p[contains (text() ,  'third-party')]")
print (content_text.text)



