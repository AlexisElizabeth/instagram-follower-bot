import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class InstaFollower:
    def __init__(self, chrome_driver_path):
        driver_service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=driver_service)
        self.username = ""
        self.password = ""

    def login(self, instagram_username, instagram_password):
        self.username = instagram_username
        self.password = instagram_password
        url = "https://www.instagram.com/"
        self.driver.get(url)
        time.sleep(2)
        cookies = self.driver.find_elements(By.TAG_NAME, value="button")[7]
        cookies.click()
        time.sleep(1)
        username_input = self.driver.find_element(By.NAME, value="username")
        username_input.click()
        username_input.send_keys(self.username)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.click()
        password_input.send_keys(self.password)
        time.sleep(1)
        submit_button = self.driver.find_elements(By.CSS_SELECTOR, value="button")[1]
        submit_button.click()
        time.sleep(8)
        not_now = self.driver.find_element(By.XPATH, value='//button[normalize-space()="Not now"]')
        not_now.click()
        time.sleep(2)
        not_now = self.driver.find_elements(By.CSS_SELECTOR, value='._a9-v button')[1]
        not_now.click()
        time.sleep(1)

    def find_followers(self, similar_account):
        self.driver.get(f"https://www.instagram.com/{similar_account}")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div[1]/div/'
                                                             'div/div/div[1]/div[2]/div[2]/section/main/'
                                                             'div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(3)
        scr1 = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/'
                                                  'div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(1)

    def follow(self):
        time.sleep(2)
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='button')[5:]
        for button in all_buttons:
            button.click()
            try:
                cancel = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div/div[2]/"
                                                                  "div/div/div[2]/div/div/div[1]/div/div[2]/"
                                                                  "div/div/div/div/div[2]/div/div/div[3]/button[2]")
            except selenium.common.exceptions.NoSuchElementException:
                pass
            else:
                cancel.click()
        time.sleep(1000)
