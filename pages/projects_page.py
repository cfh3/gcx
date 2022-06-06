import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class ProjectsPage():
    #my_project_css_selector = '.hKDyKW'
    my_project_css_selector = '#__next > div > div.sc-kyCyAI.eCdcCn > div.sc-fEVUGC.dZEpeg > div.sc-dchYKM.sc-jLrYHE.bGnBJH > div > div.sc-fqCOlO.cxaymw > div > div > div.sc-uJMKN.daoARj > a > div:nth-child(2) > div > div > div'

    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def get_my_project(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.my_project_css_selector)