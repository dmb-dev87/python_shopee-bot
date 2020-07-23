import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, username, password):
        print('Getting the Browser...')
        browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        browser.get('https://shopee.com.my/buyer/login')

        print('Click language button...')
        self.click_LangBtn(browser)

        print('Login to site...')
        self.log_In(browser, username, password)

        print('Complete...')
    
    def click_LangBtn(self, browser):
        lang_btn = browser.find_element_by_xpath("//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")
        lang_btn.click()
        time.sleep(5)

    def log_In(self, browser, username, password):
        name_input = browser.find_element_by_name('loginKey')
        name_input.send_keys(username)
        time.sleep(5)

        pwd_input = browser.find_element_by_name('password')
        pwd_input.send_keys(password)
        time.sleep(5)

        loginBtn = browser.find_element_by_xpath("//button[contains(., 'Login')]")
        loginBtn.click()

        return

Username = input('Paste the username here: ')
Password = input('Paste the password here: ')
Login(Username, Password)