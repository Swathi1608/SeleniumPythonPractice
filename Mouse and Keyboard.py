import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

search = driver.find_element(by = By.CLASS_NAME, value = "gLFyf")
#search.send_keys("Anthropic")
#time.sleep(2)
action = ActionChains(driver)

#double click in mouse
#action.double_click(search).perform()
#time.sleep(2)

#right click in mouse
#action.context_click(search).perform()
#time.sleep(3)

#mouse hover
#search_by_voice = driver.find_element(by = By.XPATH, value = "//div[@aria-label='Search by voice']")
#action.move_to_element(search_by_voice).perform()
#time.sleep(3)
#search_by_voice.click()
#time.sleep(3)

#drag and drop
#source = driver.find_element(by = By.XPATH, value = "//a[text() = 'हिन्दी']")
#target = driver.find_element(by = By.CLASS_NAME, value = "gLFyf")
#action = ActionChains(driver)
#action.drag_and_drop(source,target).perform()
#time.sleep(5)

#keyboard enter and backspace
search = driver.find_element(by = By.CLASS_NAME, value = "gLFyf")
search.send_keys("Anthropic C")
time.sleep(2)
action = ActionChains(driver)
action.send_keys(Keys.BACKSPACE).perform()
time.sleep(3)
action.send_keys(Keys.ENTER).perform()
time.sleep(3)





