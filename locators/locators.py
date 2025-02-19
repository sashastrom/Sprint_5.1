from selenium.webdriver.common.by import By

# https://stellarburgers.nomoreparties.site/register
enter_reg_name = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
enter_reg_email = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
enter_reg_password = (By.XPATH, "//input[@name='Пароль' and @type='password' and @class='text input__textfield text_type_main-default']")
click_reg_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
enter_button_after_reg = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']")
not_correct_password = (By.XPATH, ".//p[contains(@class, 'input__error')]")

#https://stellarburgers.nomoreparties.site/login
login_text = (By.XPATH, ".//h2[text()='Вход']")
login_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
login_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
click_login_button = (By.XPATH, ".//button[text()='Войти']")
order_button_main= (By.XPATH, ".//button[text()='Оформить заказ']")
personal_account_button_main = (By.XPATH, ".//p[text()='Личный Кабинет']")
login_button_from_reg = (By.CLASS_NAME, "Auth_link__1fOlj")
enter_to_account_main = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт') and contains(@class, 'button_button__33qZ0')]")
forgot_password_button = (By.CLASS_NAME, "Auth_link__1fOlj")
enter_button_from_forgot_password_page = (By.XPATH, ".//a[text()='Войти']")

#https://stellarburgers.nomoreparties.site/account/profile
personal_area_text = (By.XPATH, ".//p[text()='Личный Кабинет']")
personal_data = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
order_history = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
main_title_of_constructor = ((By.CSS_SELECTOR, "h1[class*='text_type_main-large']"))
logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
logout_button = (By.XPATH, ".//button[text()='Выход']")
account_info_text = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")
logo_tag_set_burger = (By.XPATH, ".//h1")

#https://stellarburgers.nomoreparties.site/
# constructor
buns_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
buns_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
fillings_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
sauces_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")