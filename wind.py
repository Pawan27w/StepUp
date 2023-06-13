import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")

driver.find_element(By.XPATH,"//button[@id='newTabBtn']").click()

window=driver.window_handles
first_w=window[0]
sencond_w=window[1]


driver.switch_to.window(first_w)
print("first_w",driver.title)

driver.switch_to.window(sencond_w)
print("second-w",driver.title)
#driver.switch_to.window(parentwin)

for i in window:
    driver.switch_to.window(sencond_w)
    if driver.title=="AlertsDemo - H Y R Tutorials":
        driver.close()