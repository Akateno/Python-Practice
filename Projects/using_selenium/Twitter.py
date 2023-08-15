from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time 


PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL="theGapBackup"
TWITTER_PASSWORD="Jobseeker1!"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CHROME_DRIVER_PATH=Service("/Users/erickvargas/Development/chrome_driver/chromedriver")

class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.driver=webdriver.Chrome(service=CHROME_DRIVER_PATH)
        self.up=0
        self.down=0 


    # def get_internet_speed(self):
    #     self.driver.get("https://www.speedtest.net/")
    #     time.sleep(3)
    #     go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
    #     go_button.click()

    #     time.sleep(60)
    #     self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
    #     self.down=self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
    #     print(self.up,self.down)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        # email=self.driver.find_element(By.XPATH, '//input[contains(@name,"text")]')
        email=self.driver.find_element(By.NAME, 'text')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
       
        email.send_keys(Keys.ENTER)
        password=self.driver.find_element(By.Name,'password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        locate_tweet_position = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        locate_tweet_position.click()
        locate_tweet_position.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        sleep(10)
        self.driver.close()

        

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()










# driver=webdriver.Chrome(service=chrome_driver_path)
# driver.get("https://twitter.com/i/flow/login")


# username=driver.find_element(By.NAME, 'text')
# username.send_keys(TWITTER_EMAIL)
# username.send_keys(Keys.ENTER)


