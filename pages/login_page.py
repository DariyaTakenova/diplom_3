from pages.base_page import BasePage
from locators import LoginPageLocators
from data import USER_EMAIL, USER_PASSWORD

class LoginPage(BasePage):
    # Ввод email
    def input_email(self, email=USER_EMAIL):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)

    # Ввод пароля
    def input_password(self, password=USER_PASSWORD):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)

    # Нажать кнопку "Войти"
    def submit_login(self):
        self.click(LoginPageLocators.SUBMIT_BUTTON)

    # Полный процесс авторизации
    def login(self, email=USER_EMAIL, password=USER_PASSWORD):
        self.input_email(email)
        self.input_password(password)
        self.submit_login()
