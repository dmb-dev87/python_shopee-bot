import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Favorite:
    def __init__(self, product_Url):
        print('Visit product_Url')
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        browser.get(product_Url)

        print('Click language button...')
        self.click_LangBtn(browser)

        print('Click favorite...')
        self.click_Favorite(browser)

        print('Complete...')

    def click_LangBtn(self, browser):
        lang_btn = browser.find_element_by_xpath("//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")
        lang_btn.click()
        time.sleep(5)

    def click_Favorite(self, browser):
        fav_element = browser.find_element_by_xpath('//div[@class="_25DJo1"]/*[name()="svg"][@fill="none"]')
        if fav_element is None:
            return

        fav_element.click()
        time.sleep(5)

product_Url = input('Paste the product url here: ')
Favorite(product_Url)