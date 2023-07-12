from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path=Service("/Users/erickvargas/Development/chrome_driver/chromedriver")
driver=webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.linkedin.com/uas/login?fromSignIn=true&trk=reset_password")


# sign_in=driver.find_element(By.LINK_TEXT,"Sign in")
# sign_in.click()

user_name=driver.find_element(By.ID, "username")
user_name.send_keys("erickkvargas@gmail.com")
password=driver.find_element(By.ID, "password")
password.send_keys("Rockbreaker11")
second_sign_in=driver.find_element(By.TAG_NAME, "button")
second_sign_in.click()


# jobs=driver.find_element(By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')
# jobs.click()

# search_jobs=driver.find_element(By.CSS_SELECTOR,'.relative input')
# search_jobs.send_keys("software engineer")
# search_jobs.send_keys(Keys.ENTER)

homepage_searchbox = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
homepage_searchbox.send_keys("Software developer")
homepage_searchbox.send_keys(Keys.ENTER)

#click remote 
easy_apply=driver.find_element(By.LINK_TEXT, 'Easy apply')
easy_apply.click()





experience=driver.find_element(By.XPATH, '//*[@id="ember779"]/button')
experience.click()

entry=driver.find_element(By.ID,"experience-2")
entry.click()

date_posted=driver.find_element(By.XPATH, '//*[@id="ember5974"]/button')
date_posted.click()


past_week=driver.find_element(By.ID, "timePostedRange-r604800")
past_week.click()

results=driver.find_element(By.ID,'ember6144')
results.click()


time.time()+5

driver.quit()
