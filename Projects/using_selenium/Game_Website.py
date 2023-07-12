from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path=Service("/Users/erickvargas/Development/chrome_driver/chromedriver")
driver=webdriver.Chrome(service=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout_duration=60
verification=5

#find the cookie 
cookie=driver.find_element(By.ID, "cookie")


while True:
    cookie.click()
    
    if timeout_duration < time.time():
        print(time.time())
        timeout_duration=time.time() + 5
       
        
driver.quit()







