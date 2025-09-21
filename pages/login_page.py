import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    """PageObject для страницы логина"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email: str) -> None:
        """Вводит email пользователя"""
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password: str) -> None:
        """Вводит пароль пользователя"""
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self) -> None:
        """Кликает по кнопке входа"""
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Переход на страницу регистрации")
    def go_to_register(self) -> None:
        """Кликает на ссылку 'Зарегистрироваться'"""
        self.click(LoginPageLocators.REGISTER_LINK)

    @allure.step("Получаем сообщение об ошибке")
    def get_error_message(self) -> str:
        """Возвращает текст ошибки"""
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)