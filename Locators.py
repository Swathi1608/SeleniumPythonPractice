import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://www.facebook.com/")
time.sleep(2)

# find element by ID
#email_1 = driver.find_element(by=By.ID, value ="64qjbjb9pb6amH1")
#email_1.send_keys("r.swathiraj99@gmail.com")
#time.sleep(2)
#email_1.clear()
#time.sleep(2)

#find element by Name
#email_1 = driver.find_element(by=By.NAME, value ="email")
#email_1.send_keys("r.swathiraj99@gmail.com")
#time.sleep(2)
#n some modern web applications, .clear() may not work due to JavaScript-controlled inputs. In such cases, I use CTRL + A and DELETE via send_keys() for reliable clearing
#email_1.send_keys(Keys.CONTROL + "a", Keys.DELETE)


#find element by class name
#email_1 = driver.find_element(by=By.CLASS_NAME, value ="")
#email_1.send_keys("r.swathiraj99@gmail.com")
#time.sleep(2)
#email_1.clear()
#time.sleep(2)

#find element by xpath
#email_1 = driver.find_element(by=By.XPATH, value ="//input[@name='email']")
#email_1.send_keys("r.swathiraj99@gmail.com")
#time.sleep(2)
#n some modern web applications, .clear() may not work due to JavaScript-controlled inputs. In such cases, I use CTRL + A and DELETE via send_keys() for reliable clearing
#email_1.send_keys(Keys.CONTROL + "a", Keys.DELETE)
#time.sleep(3)

#find element by LINK TEXT
#password = driver.find_element(by=By.LINK_TEXT, value = "Forgotten password?")
#password.click()
#time.sleep(2)

#find element by PARTIAL LINK TEXT
#password = driver.find_element(by=By.PARTIAL_LINK_TEXT, value = "Forgotten")
#password.click()
#time.sleep(2)

#find element by CSS Selector - id
#email = driver.find_element(By.CSS_SELECTOR, '#_R_1cl2p4jikacppb6amH1_')
#email.send_keys("r.swathiraj99@gmail.com")
#time.sleep(3)

# find text in webpage
fb_text = driver.find_element(by = By.XPATH, value = "//*[text()='Log in to Facebook']")
actual_text = fb_text.text
print("Text is --> ", actual_text)
assert "to" in actual_text, "Text not available"
time.sleep(5)

