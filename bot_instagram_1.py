from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests


class Bot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        name = driver.find_element_by_name('username').send_keys(username)
        pas = driver.find_element_by_name('password').send_keys(password)
        btn_1 = driver.find_element_by_css_selector('button[type="submit"]').click()
        # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
        # username.click()
        # username.send_keys(username)
        time.sleep(10)
        btn_2 = driver.find_element_by_css_selector('button[type="button"]').click()
        time.sleep(10)
        btn_3 = driver.find_element_by_css_selector('button.HoLwm').click()

    def like(self):
        driver = self.driver
        time.sleep(5)
        driver.get("https://www.instagram.com/hossein.valian/")
        time.sleep(10)
        driver.find_element_by_class_name("v1Nh3").click()
        time.sleep(10)
        i = 1
        while 1 <= 10:
            time.sleep(5)
            if driver.find_elements_by_xpath('//*[contains(@aria-label,"Unlike")]'):
                time.sleep(3)
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            elif driver.find_elements_by_xpath('//*[contains(@aria-label,"Like")]'):
                time.sleep(15)
                driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')[
                    0].click()
                driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i += 1
        driver.get("https://www.instagram.com/hossein.valian/")

    def comment(self):
        driver = self.driver
        driver.get('https://www.instagram.com/python.hub/')
        time.sleep(50)
        post = driver.find_element_by_css_selector('a[href="/p/CJsEYS1glQv/"]').click()
        i = 1
        while i <= 5:
            time.sleep(50)

            waits = WebDriverWait(driver, 50)
            text = waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            text.click()
            text = waits.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Ypffh')))
            text.send_keys("hi" + Keys.ENTER)
            next = driver.find_element_by_link_text('next').click()
            i += 1
            driver.get('https://www.instagram.com/python.hub/')


username = ""
password = ""
test = Bot(username, password)
test.login()
test.like()
