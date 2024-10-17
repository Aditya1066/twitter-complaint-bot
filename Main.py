from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

email = "<YOUR_EMAIL>"
password = "<YOUR_PASSWORD>>"
username = "<YOUR_USERNAME>>"
promissed_down = 150
promissed_up = 10




class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        self.driver.get(url)
        time.sleep(5)
        go = self.driver.find_element(By.CSS_SELECTOR, '#container > div.pre-fold > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a')
        go.click()
        time.sleep(60)
        d = self.driver.find_element(By.CSS_SELECTOR, '#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span')
        u = self.driver.find_element(By.CSS_SELECTOR, '#container > div.pre-fold.mobile-test-complete > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-left > div > div.result-data.u-align-left > span')
        self.down = d.text
        self.up = u.text
        print(self.down,"\n",self.up)



    def tweet_at_provider(self):
        url2 = "https://x.com/home"
        self.driver.get(url2)
        time.sleep(5)
        b1 = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo > div > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a')
        self.driver.execute_script("arguments[0].scrollIntoView();", b1)
        b1.click()
        time.sleep(5)
        inp1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label')
        inp1.send_keys(email, Keys.ENTER)
        time.sleep(5)
        unu = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label')
        unu.send_keys(username, Keys.ENTER)
        time.sleep(5)
        inp2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label')
        inp2.send_keys(password, Keys.ENTER)
        time.sleep(5)
        inp3 = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        inp3.send_keys(f"Hey Internet Porvider my internet speed is down:{self.down} \n up:{self.up}")
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
