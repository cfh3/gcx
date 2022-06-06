import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage


@pytest.fixture
def browser():
  options = Options()
  options.headless = False
  ser = Service("/usr/local/bin/chromedriver")
  driver = webdriver.Chrome(service=ser, options=options)
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()

    email_address_field = login_page.get_email_address_field()
    password_field = login_page.get_password_field()
    login_button = login_page.get_login_button()
    
    email_address_field.send_keys(os.getenv('GCXUSERNAME'))
    password_field.send_keys(os.getenv('GCXPASSWORD'))
    login_button.click()
    
    # TODO: remove the sleep and figure out how to tell if the login succeeded
    time.sleep(5)