from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 


chrome_driver_path=Service("/Users/erickvargas/Development/chrome_driver/chromedriver")
op = webdriver.ChromeOptions()
driver=webdriver.Chrome(service=chrome_driver_path, options=op)
# driver.find_element(By.CSS_SELECTOR)
# driver.find_element(By.XPATH)



driver.get("https://www.python.org/")


# price=driver.find_element(By.ID, "priceblock-ourprice")
# print(price.text)

# logo=driver.find_element(By.CLASS_NAME, "python-logo")

# documentation_link=driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link=driver.find_element(By.XPATH, '//*[@id="close-python-network"]')
# print(bug_link.text)

# search_bar=driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute('placeholder'))

# driver.find_elements(By.CLASS_NAME, "example")

event_times=driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# for time in event_times:
#     print(time.text)

event_names=driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
# for name in event_names:
#     print(name.text)

events={}

for n in range(len(event_times)):
    events[n]= {

        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

#driver.close()
driver.quit()

