from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import time
import libraries.login as login

class Product:
    def __init__(self, url, username, password):
        self.Product_Url = url
        self.Username = username
        self.Password = password

    def click_LangBtn(self, browser):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                         "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")))
        browser.find_element_by_xpath(
            "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]").click()
        time.sleep(5);

    def visit(self, idle_time):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')

        browser.get(self.Product_Url)
        self.click_LangBtn(browser)

        login_link = browser.find_element_by_xpath("//a[contains(., 'Login')]")

        if login_link is None:
            return
        else:
            login_url = login_link.get_attribute('href')
            browser.get(login_url)

            user_log = login.Login(self.Username, self.Password)
            user_log.log_In(browser)

            time.sleep(idle_time)
            browser.close()

    def favorite(self, idle_time):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        wait = WebDriverWait(browser, idle_time)

        browser.get(self.Product_Url)
        self.click_LangBtn(browser)

        login_link = browser.find_element_by_xpath("//a[contains(., 'Login')]")

        if login_link is None:
            return

        login_url = login_link.get_attribute('href')
        browser.get(login_url)

        user_log = login.Login(self.Username, self.Password)
        user_log.log_In(browser)

        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Favorite")]')))
            try:
                fav_element = browser.find_element_by_xpath(
                    '//*[name()="svg"][@class="_10K0Ee"]/*[name()="path"][@fill="none"]')
                ActionChains(browser).move_to_element(fav_element).click().perform()
                time.sleep(idle_time)
            except NoSuchElementException:
                time.sleep(idle_time)
        except TimeoutException:
            time.sleep(idle_time)

        browser.close()
