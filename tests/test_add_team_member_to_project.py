import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.projects_page import ProjectsPage
from pages.login_page import LoginPage
from pages.project_details_page import ProjectDetailsPage
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

def login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    
    email = login_page.get_email_address_field()
    password = login_page.get_password_field()
    login_button = login_page.get_login_button()

    email.send_keys('chiphofmann@gmail.com')
    password.send_keys('big.yellow.roof')
    login_button.click()

def test_add_team_member(browser):
    login(browser)
    
    projects_page = ProjectsPage(browser)
    my_project = projects_page.get_my_project()
    my_project.click()
    
    project_details_page = ProjectDetailsPage(browser)
    team_button = project_details_page.get_team_button()
    team_button.click()
    
    add_team_member = project_details_page.get_add_team_member()
    add_team_member.click()
    team_member_first_name = project_details_page.get_team_member_first_name_field()
    team_member_last_name = project_details_page.get_team_member_last_name_field()
    team_member_email_address = project_details_page.get_team_member_email_address_field()
    add_team_member_button = project_details_page.get_add_team_member_button()
    team_member_first_name.send_keys('Skip')
    team_member_last_name.send_keys('Heffman')
    team_member_email_address.send_keys('skip@heffman.org')
    # add_team_member_button.click()
    time.sleep(5)

