import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators import RegisterPageLocators


class RegisterPage(BasePage):
    """PageObject для страницы регистрации"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Вводим имя: {name}")
    def enter_name(self, name: str) -> None:
        """Вводит имя пользователя"""
        self.input_text(RegisterPageLocators.NAME_INPUT, name)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email: str) -> None:
        """Вводит email"""
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def enter_password(self, password: str) -> None:
        """Вводит пароль"""
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку 'Зарегистрироваться'")
    def click_register_button(self) -> None:
        """Кликает по кнопке регистрации"""
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Переходим на страницу логина")
    def go_to_login(self) -> None:
        """Кликает на ссылку 'Войти'"""
        self.click(RegisterPageLocators.LOGIN_LINK)

    @allure.step("Получаем сообщение об ошибке")
    def get_error_message(self) -> str:
        """Возвращает текст ошибки при неудачной регистрации"""
        return self.get_text(RegisterPageLocators.ERROR_MESSAGE)
