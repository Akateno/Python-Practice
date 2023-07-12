from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


chrome_driver_path=Service("/Users/erickvargas/Development/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()

driver=webdriver.Chrome(service=chrome_driver_path, options=op)
# driver.find_element(By.CSS_SELECTOR)
# driver.find_element(By.XPATH)



# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# count=driver.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
# print(count.text)


# all_portals = driver.find_element(By.LINK_TEXT, 'Content portals')
# all_portals.click()

# search_bar=driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name=driver.find_element(By.NAME, "fName")
first_name.send_keys("Tony")

last_name=driver.find_element(By.NAME, "lName")
last_name.send_keys("Bolony")
timeout=time.time()+5
email=driver.find_element(By.NAME, "email")
email.send_keys("tonybalony@gmail.com")


sign_up=driver.find_element(By.TAG_NAME, "button")
sign_up.click()



five_min=time.time()+60*5



driver.quit()