import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage():
    URL = 'https://app.staging.guidecx.io/auth/login'
    
    email_address_field_id = 'input_1'
    password_field_id = 'input_2'
    login_button_css_selector = '.MuiButtonBase-root'
    
    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def get_email_address_field(self):
        return self.browser.find_element(By.ID, self.email_address_field_id)
    
    def get_password_field(self):
        return self.browser.find_element(By.ID, self.password_field_id)

    def get_login_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.login_button_css_selector)