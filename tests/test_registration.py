import pytest
import allure
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
from data import Data
import random
import string


def generate_unique_email():
    """Генерирует уникальный email для регистрации"""
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"test_{random_part}@yandex.ru"


@allure.feature("Регистрация")
class TestRegistration:

    @allure.story("Успешная регистрация")
    def test_successful_registration(self, driver):
        main_page = MainPage(driver)
        reg_page = RegistrationPage(driver)

        email = generate_unique_email()
        password = Data.VALID_PASSWORD

        with allure.step("Открыть форму регистрации"):
            main_page.open_registration_form()

        with allure.step("Заполнить форму валидными данными"):
            reg_page.register(Data.VALID_NAME, email, password)

        with allure.step("Проверить, что открылся экран входа"):
            assert reg_page.is_login_form_visible(), "Форма входа не открылась после регистрации"

    @allure.story("Ошибка при коротком пароле")
    def test_registration_with_short_password(self, driver):
        main_page = MainPage(driver)
        reg_page = RegistrationPage(driver)

        email = generate_unique_email()

        with allure.step("Открыть форму регистрации"):
            main_page.open_registration_form()

        with allure.step("Заполнить форму с коротким паролем"):
            reg_page.register(Data.VALID_NAME, email, Data.INVALID_PASSWORD_SHORT)

        with allure.step("Проверить сообщение об ошибке"):
            assert reg_page.is_password_error_visible(), "Нет сообщения об ошибке при коротком пароле"