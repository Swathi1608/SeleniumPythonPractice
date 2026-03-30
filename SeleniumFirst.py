import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Method 1 to launch browser

#print('Start')
#driver = webdriver.Chrome()
#driver.get("https://www.google.com")
#time.sleep(5)
#print("Done")

#Method 2 to launch browser

#service_obj =  Service()
#driver = webdriver.Chrome(service = service_obj)
#driver.get("https://www.google.com")
#time.sleep(5)

#Method 3 to launch browser

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://www.google.com")
time.sleep(2)

#Maximize Window
#driver.maximize_window()
#time.sleep(3)

#Minimize Window
#driver.minimize_window()
#time.sleep(3)

#Close Window
#driver.close()

#Verify Title and Assertion
#title = driver.title
#print("Title is -->", title)
#assert title == "Googlee" , f"Title doesn't match, expected is Googlee but actual is {title}"

#Find element using locators

search = driver.find_element(by=By.NAME, value="q")
search.send_keys("Pankaj Gupta Udemy")
time.sleep(3)
search_btn = driver.find_element(by=By.XPATH, value="(//input[@value='Google Search'])[1]")
search_btn.click()
time.sleep(5)

# Go backward in Browser
driver.back()
time.sleep(2)

#Referesh the page in browser
driver.refresh()
time.sleep(2)

#Go forward in the browser
driver.forward()
time.sleep(2)


