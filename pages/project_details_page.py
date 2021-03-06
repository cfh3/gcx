import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class ProjectDetailsPage():
    team_button_css_selector = 'button.MuiButtonBase-root:nth-child(5) > span:nth-child(1)'
    add_team_member_css_selector = '#__next > div > div.sc-kyCyAI.eCdcCn > div.sc-fEVUGC.dZEpeg > div.sc-dchYKM.sc-jLrYHE.bGnBJH > div > div.sc-fqCOlO.cxaymw > div > div.sc-cSHVUG.sc-ksYbfQ.dBIxSO > div:nth-child(2) > span > a > button'
    team_member_first_name_field_css = "/html/body/div[4]/div[3]/div/div[2]/form/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/input" 
    team_member_last_name_field_css = "/html/body/div[4]/div[3]/div/div[2]/form/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/input"
    team_member_email_field_css = "/html/body/div[4]/div[3]/div/div[2]/form/div/div/div/div/div/div/div[2]/div/div[3]/div/div[2]/input"
    add_team_member_button_css_selector = 'body > div:nth-child(64) > div.MuiPaper-root.MuiDrawer-paper.MuiDrawer-paperAnchorRight.MuiPaper-elevation16 > div > div.sc-jwKygS.hbDVPS > button'
                                            
    def __init__(self, browser):
        self.browser = browser
    
    def load(self):
        self.browser.get(self.URL)
    
    def get_team_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.team_button_css_selector)
    
    def get_add_team_member_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.add_team_member_css_selector)

    def get_team_member_first_name_field(self):
        return self.browser.find_element(By.XPATH, self.team_member_first_name_field_css)
    
    def get_team_member_last_name_field(self):
        return self.browser.find_element(By.XPATH, self.team_member_last_name_field_css)
    
    def get_team_member_email_address_field(self):
        return self.browser.find_element(By.XPATH, self.team_member_email_field_css)
    
    def get_add_team_members_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, self.add_team_member_button_css_selector)