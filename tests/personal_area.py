from conftest import *
from test_project_data.page_url import *
from locators.locators import *

class TestPersonalArea:
    def test_transfer_to_personal_area(self,login):
        driver = login
        assert driver.current_url == main_page_url
        driver.find_element(*personal_area_text).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(personal_data))
        profile = driver.find_element(*order_history)
        assert driver.current_url == profile_url
        assert profile.text == 'История заказов'

    def test_transfer_from_personal_area_to_constructor(self,login):
        driver = login
        driver.find_element(*personal_area_text).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(personal_data))
        driver.find_element(*constructor_button).click()
        main_title = driver.find_element(*main_title_of_constructor)
        assert main_title.text == 'Соберите бургер'

    def test_transfer_clicking_logo(self,login):
        driver = login
        driver.find_element(*personal_area_text).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(personal_data))
        driver.find_element(*logo).click()
        h1_tag = driver.find_element(*logo_tag_set_burger)
        assert h1_tag.text == 'Соберите бургер'

    def test_exit_from_personal_area(self,login):
        driver = login
        driver.find_element(*personal_account_button_main).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(account_info_text))
        driver.find_element(*logout_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(login_text))
        assert driver.current_url == login_url
        text_check = driver.find_element(*login_text)
        assert text_check.text == 'Вход'