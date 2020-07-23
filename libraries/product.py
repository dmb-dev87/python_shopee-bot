from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
import libraries.login as login

class Product:
    def __init__(self, url, username, password):
        print('Product Init')
        self.Product_Url = url
        self.Username = username
        self.Password = password

    def click_LangBtn(self, browser):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                         "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")))
        browser.find_element_by_xpath(
            "//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]").click()
        time.sleep(5);

    def visit(self):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')

        browser.get(self.Product_Url)
        self.click_LangBtn(browser)

        print('Login...')
        login_link = browser.find_element_by_xpath("//a[contains(., 'Login')]")

        if login_link is None:
            print('Cant find the login link')
            return True
        else:
            print('Go to login url')
            login_url = login_link.get_attribute('href')
            print(login_url)

            browser.get(login_url)
            # wait.until(EC.url_changes(login_url))

            user_log = login.Login(self.Username, self.Password)
            result = user_log.log_In(browser)
            print(result)

    def favorite(self):
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        wait = WebDriverWait(browser, 10)

        browser.get(self.Product_Url)
        self.click_LangBtn(browser)

        print('Login...')
        login_link = browser.find_element_by_xpath("//a[contains(., 'Login')]")

        if login_link is None:
            print('Cant find the login link')
            return True
        else:
            print('Go to login url')
            login_url = login_link.get_attribute('href')
            print(login_url)

            browser.get(login_url)
            # wait.until(EC.url_changes(login_url))

            user_log = login.Login(self.Username, self.Password)
            result = user_log.log_In(browser)
            print(result)

            wait.until(EC.url_changes(self.Product_Url))
            print('Wait favorite...')
            element_present = EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Favorite")]'))
            WebDriverWait(browser, 10).until(element_present)
            # wait.until(lambda x: x.find_element_by_class("_10K0Ee"))
            print('Find svg element...')

            try:
                fav_element = browser.find_element_by_xpath('//*[name()="svg"][@class="_10K0Ee"]/*[name()="path"][@fill="none"]')
                ActionChains(browser).move_to_element(fav_element).click().perform()
            except NoSuchElementException:
                time.sleep(5)

            time.sleep(5)
            browser.close()
