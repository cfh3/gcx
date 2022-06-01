import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

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
    
    email_address_field.send_keys('chiphofmann@gmail.com')
    password_field.send_keys('big.yellow.roof')
    login_button.click()

    time.sleep(5)