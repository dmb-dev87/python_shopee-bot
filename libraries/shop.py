from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import libraries.login as login

class Shop:
    def __init__(self, url, username, password):
        self.Shop_Url = url
        self.Username = username
        self.Password = password

    def click_LangBtn(self, browser):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                         "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")))
        browser.find_element_by_xpath(
            "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]").click()
        time.sleep(5);

    def follow(self, idle_time):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        wait = WebDriverWait(browser, idle_time)

        browser.get(self.Shop_Url)
        self.click_LangBtn(browser)

        login_link = browser.find_element_by_xpath("//a[contains(., 'Login')]")

        if login_link is None:
            return
        else:
            login_url = login_link.get_attribute('href')
            browser.get(login_url)
            user_log = login.Login(self.Username, self.Password)
            user_log.log_In(browser)

            wait.until(EC.url_changes(self.Shop_Url))
            element_present = EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "follow")]'))
            wait.until(element_present)

            try:
                browser.find_element_by_xpath('//button[contains(text(), "following")]')
            except NoSuchElementException:
                follow_btn = browser.find_element_by_xpath('//button[contains(text(), "follow")]')
                follow_btn.click()

            time.sleep(idle_time)
            browser.close()

    def visit(self, idle_time):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        browser.get(self.Shop_Url)
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
