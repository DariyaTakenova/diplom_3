import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    """PageObject для главной страницы Stellar Burgers"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Открываем главную страницу")
    def open(self, url: str) -> None:
        """Открывает главную страницу"""
        self.driver.get(url)

    @allure.step("Переход в Конструктор")
    def open_constructor(self) -> None:
        """Кликает на кнопку 'Конструктор'"""
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в Ленту заказов")
    def open_order_feed(self) -> None:
        """Кликает на кнопку 'Лента заказов'"""
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Переход на страницу логина")
    def go_to_login(self) -> None:
        """Кликает на кнопку 'Войти в аккаунт'"""
        self.click(MainPageLocators.LOGIN_BUTTON)
