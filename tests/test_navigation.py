import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage
from constants import Urls


@allure.suite("Тесты навигации")
@pytest.mark.usefixtures("driver")
class TestNavigation:
    """Набор автотестов для проверки переходов между основными разделами сайта."""

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_constructor_navigation(self, driver: WebDriver) -> None:
        """Проверяем, что по клику на кнопку 'Конструктор' открывается страница конструктора."""
        driver.get(Urls.FEED_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        main_page.click_constructor()

        assert driver.current_url == Urls.MAIN_PAGE, "Не удалось перейти на страницу конструктора."

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_feed_orders_navigation(self, driver: WebDriver) -> None:
        """Проверяем, что по клику на кнопку 'Лента заказов' открывается страница ленты заказов."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        main_page.click_feed_orders()

        assert driver.current_url == Urls.FEED_PAGE, "Не удалось перейти на страницу ленты заказов."
