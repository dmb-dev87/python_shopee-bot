import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'byszstore'
passwordStr = 'Magix007'

browser = webdriver.Chrome(executable_path='./chromedriver.exe')
browser.get('https://shopee.com.my/buyer/login')

lang_btn = browser.find_element_by_xpath("//div[@class='language-selection__list-item' and .//button[contains(., 'English')]]")
lang_btn.click()
time.sleep(5)

# fill in username and hit the next button

username = browser.find_element_by_name('loginKey')
username.send_keys(usernameStr)
time.sleep(5)

password = browser.find_element_by_name('password')
password.send_keys(passwordStr)
time.sleep(5)

loginBtn = browser.find_element_by_xpath("//button[contains(., 'Login')]")
loginBtn.click()
