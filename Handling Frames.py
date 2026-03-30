import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://vinothqaacademy.com/iframe/")
driver.implicitly_wait(10)

driver.switch_to.frame("employeetable")
frame_content = driver.find_element(by = By.ID, value = "nameInput")
frame_content.send_keys("Swathi")
time.sleep(5)
driver.switch_to.default_content()

driver.switch_to.frame("popuppage")
alert = driver.find_element(by= By.XPATH,value="//button[text() ='Alert Box']")
alert.click()
time.sleep(5)
alert_1 = driver.switch_to.alert
alert_1.accept()
time.sleep(5)
result = driver.find_element(by=By.ID, value="demotwo")
actual_result = result.text
assert actual_result == "You clicked on OK!", "Text Not Matched"
print("Text Matched")
time.sleep(5)
