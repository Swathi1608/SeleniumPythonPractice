import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service_obj =  Service("D:\Selenium Practice\Browser Drivers\chromedriver-win64\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)

#switching between windows
click_here = driver.find_element(by = By.LINK_TEXT, value = 'Click Here')
click_here.click()
time.sleep(3)
parent_window = driver.current_window_handle
print("Parent Window is --> ", parent_window)
parent_screen = driver.find_element(by = By.TAG_NAME, value = 'h3')
print(parent_screen.text)
time.sleep(3)
all_windows = driver.window_handles
print("All windows are --> ", all_windows)
time.sleep(3)
for window in all_windows:
    if parent_window != window:
        driver.switch_to.window(window)
        print("Child Window is --> ", window)
        child_screen = driver.find_element(by=By.TAG_NAME, value='h3')
        print(child_screen.text)
        assert "New Window" in child_screen.text, "Switch didn't happen"
        driver.close()
#switch to parent window from child window
driver.switch_to.window(parent_window)
time.sleep(3)
print("Switched to Parent Window")
print("After switching to parent window ", parent_screen.text)




