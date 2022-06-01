import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class ProjectsPage():
    my_project_css_selector = '.hKDyKW'

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def get_my_project(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.my_project_css_selector)