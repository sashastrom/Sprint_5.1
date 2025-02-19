import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_project_data.data import LoginData
from test_project_data.page_url import *
from locators.locators import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(main_page_url)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(login_url)
    driver.find_element(*login_email_field).send_keys(LoginData.email)
    driver.find_element(*login_password_field).send_keys(LoginData.password)
    driver.find_element(*click_login_button).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(order_button_main))
    return driver