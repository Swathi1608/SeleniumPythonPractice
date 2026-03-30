import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

#accepting alert
#alert = driver.find_element(by= By.XPATH,value="//button[@onclick='jsAlert()']")
#alert.click()
#time.sleep(5)
#alert_1 = driver.switch_to.alert
#alert_1.accept()
#time.sleep(5)
#result = driver.find_element(by=By.ID, value="result")
#actual_result = result.text
#assert actual_result == "You successfully clicked an alert", "Text Not Matched"
#print("Text Matched")

#denying alert
#alert_2 = driver.find_element(by=By.XPATH,value="//button[@onclick='jsConfirm()']")
#alert_2.click()
#time.sleep(5)
#alert_3 = driver.switch_to.alert
#alert_3.dismiss()
#time.sleep(5)
#result_1 = driver.find_element(by=By.XPATH, value="//*[text()='You clicked: Cancel']")
#actual_result_1 = result_1.text
#assert actual_result_1 == "You clicked: Cancel", "Text Not Matched"
#print("Text Matched")

#typing text in alert
alert_4 = driver.find_element(by= By.XPATH, value="//button[@onclick='jsPrompt()']")
alert_4.click()
time.sleep(2)
alert_5 = driver.switch_to.alert
name = "Swathi"
alert_5.send_keys(name)
alert_5.accept()
time.sleep(3)
result_2 = driver.find_element(by=By.ID, value="result")
actual_result_2 = result_2.text
assert actual_result_2 == "You clicked: Swathi", "Text Not Matched"
print("Text Matched")



