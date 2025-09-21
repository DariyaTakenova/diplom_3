# tests/test_login.py

import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import Data


@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Вход через кнопку «Войти в аккаунт» на главной")
    def test_login_from_main_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Нажать кнопку 'Войти в аккаунт'"):
            main_page.click_login_button()

        with allure.step("Ввести корректные данные и войти"):
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)

        with allure.step("Проверить успешный вход (отображается кнопка 'Оформить заказ')"):
            assert main_page.is_logged_in(), "Пользователь не вошёл через кнопку на главной странице"

    @allure.story("Вход через кнопку 'Личный кабинет'")
    def test_login_from_profile_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Нажать кнопку 'Личный кабинет'"):
            main_page.click_profile_button()

        with allure.step("Ввести корректные данные и войти"):
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)

        with allure.step("Проверить успешный вход"):
            assert main_page.is_logged_in(), "Пользователь не вошёл через кнопку 'Личный кабинет'"

    @allure.story("Вход через кнопку в форме регистрации")
    def test_login_from_registration_form(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Открыть форму регистрации"):
            main_page.open_registration_form()

        with allure.step("Нажать кнопку 'Войти' внизу формы"):
            login_page.go_to_login_from_registration()

        with allure.step("Ввести корректные данные и войти"):
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)

        with allure.step("Проверить успешный вход"):
            assert main_page.is_logged_in(), "Пользователь не вошёл через форму регистрации"

    @allure.story("Вход через кнопку в форме восстановления пароля")
    def test_login_from_forgot_password_form(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Открыть форму восстановления пароля"):
            main_page.open_forgot_password_form()

        with allure.step("Нажать кнопку 'Войти'"):
            login_page.go_to_login_from_forgot_password()

        with allure.step("Ввести корректные данные и войти"):
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)

        with allure.step("Проверить успешный вход"):
            assert main_page.is_logged_in(), "Пользователь не вошёл через форму восстановления пароля"