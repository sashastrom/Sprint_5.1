from conftest import *
from test_project_data.page_url import *
from test_project_data.helpers import *

class TestRegistration:
    def test_success_registration(self,driver):
        driver.get(register_url)
        driver.find_element(*enter_reg_name).send_keys('QA Tests')
        driver.find_element(*enter_reg_email).send_keys(generate_random_email())
        driver.find_element(*enter_reg_password).send_keys('Test012')
        driver.find_element(*click_reg_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(enter_button_after_reg))
        login_button = driver.find_element(*enter_button_after_reg)
        assert driver.current_url == login_url
        assert login_button.text == 'Войти'

    def test_not_correct_password_error_for_registration(self,driver):
        driver.get(register_url)
        driver.find_element(*enter_reg_name).send_keys('Adi das')
        driver.find_element(*enter_reg_email).send_keys('adidas@testyandex.com')
        driver.find_element(*enter_reg_password).send_keys('p1')
        driver.find_element(*click_reg_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(not_correct_password))
        error_message = driver.find_element(*not_correct_password)
        assert error_message.text == 'Некорректный пароль'