from conftest import *
from locators.locators import *

class TestConstructor:
    def test_constructor_tab_sauces(self,login):
        driver = login
        sauces_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_button))
        sauces_button_element.click()
        sauces = WebDriverWait(driver, 10).until(EC.presence_of_element_located(sauces_text))
        assert sauces.text == 'Соусы'

    def test_constructor_tab_fillings(self, login):
        driver = login
        sauces_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_button))
        sauces_button_element.click()
        filling_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(filling_button))
        filling_button_element.click()
        fillings = WebDriverWait(driver, 10).until(EC.presence_of_element_located(fillings_text))
        assert fillings.text == 'Начинки'

    def test_constructor_tab_buns(self, login):
        driver = login
        sauces_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_button))
        sauces_button_element.click()
        filling_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(filling_button))
        filling_button_element.click()
        buns_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(buns_button))
        buns_button_element.click()
        buns = WebDriverWait(driver, 10).until(EC.presence_of_element_located(buns_text))
        assert buns.text == 'Булки'