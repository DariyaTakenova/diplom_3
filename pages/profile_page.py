import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators import ProfilePageLocators


class ProfilePage(BasePage):
    """PageObject для страницы профиля (личного кабинета)"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Переход в личный кабинет")
    def go_to_profile(self) -> None:
        """Кликает по ссылке 'Личный кабинет'"""
        self.click(ProfilePageLocators.PROFILE_LINK)

    @allure.step("Выход из аккаунта")
    def logout(self) -> None:
        """Кликает по кнопке 'Выход'"""
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
