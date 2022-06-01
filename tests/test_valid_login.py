import pytest, time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_1():
    lp = LoginPage
    lp.print_crap()
    ser = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=ser)
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(3)
    username = {"by": By.ID, "value": "username"} 
    driver.find_element(username["by"], username["value"]).send_keys("chip")
    time.sleep(3)
    driver.quit()