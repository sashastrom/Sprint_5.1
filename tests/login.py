from conftest import *
from locators.locators import *

class TestLogin:
    def test_login_from_main_page(self,driver):
        driver.get(login_url)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'
        driver.find_element(*login_email_field).send_keys(LoginData.email)
        driver.find_element(*login_password_field).send_keys(LoginData.password)
        driver.find_element(*click_login_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(order_button_main))
        order_button = driver.find_element(*order_button_main)
        assert order_button.text == 'Оформить заказ'
        assert driver.current_url == main_page_url

    def test_login_from_personal_account(self,driver):
        driver.get(main_page_url)
        driver.find_element(*personal_account_button_main).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'
        driver.find_element(*login_email_field).send_keys(LoginData.email)
        driver.find_element(*login_password_field).send_keys(LoginData.password)
        driver.find_element(*click_login_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(order_button_main))
        order_button = driver.find_element(*order_button_main)
        assert order_button.text == 'Оформить заказ'
        assert driver.current_url == main_page_url

    def test_login_from_registration_form(self,driver):
        driver.get(register_url)
        driver.find_element(*login_button_from_reg).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'
        driver.find_element(*login_email_field).send_keys(LoginData.email)
        driver.find_element(*login_password_field).send_keys(LoginData.password)
        driver.find_element(*click_login_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(order_button_main))
        order_button = driver.find_element(*order_button_main)
        assert order_button.text == 'Оформить заказ'
        assert driver.current_url == main_page_url

    def test_login_from_recover_password_page(self,driver):
        driver.get(main_page_url)
        driver.find_element(*enter_to_account_main).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        assert driver.current_url == login_url
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'
        driver.find_element(*forgot_password_button).click()
        driver.find_element(*enter_button_from_forgot_password_page).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'
        driver.find_element(*login_email_field).send_keys(LoginData.email)
        driver.find_element(*login_password_field).send_keys(LoginData.password)
        driver.find_element(*click_login_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(order_button_main))
        order_button = driver.find_element(*order_button_main)
        assert order_button.text == 'Оформить заказ'
        assert driver.current_url == main_page_url