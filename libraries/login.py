import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self, username, password):
        self.Username = username
        self.Password = password

    def visit(self, browser):
        self.click_LangBtn(browser)
        self.log_In(browser, self.username, self.password)

    def click_LangBtn(self, browser):
        lang_btn = browser.find_element_by_xpath("//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")

        if lang_btn is None:
            return

        lang_btn.click()
        time.sleep(5)

    def log_In(self, browser):
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'loginKey')))
        name_input = browser.find_element_by_name('loginKey')
        name_input.send_keys(self.Username)
        time.sleep(5)

        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        pwd_input = browser.find_element_by_name('password')
        pwd_input.send_keys(self.Password)
        time.sleep(5)

        loginBtn = browser.find_element_by_xpath("//button[contains(., 'Login')]")
        loginBtn.click()

        return True
