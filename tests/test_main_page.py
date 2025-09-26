import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage
from constants import Urls


@pytest.mark.usefixtures("driver")
@allure.suite("Тесты главной страницы")
class TestMainPage:
    """Набор автотестов для проверки переходов и действий на главной странице."""

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

    @allure.title("Проверка открытия и закрытия модального окна ингредиента")
    def test_ingredient_modal(self, driver: WebDriver) -> None:
        """Проверяем, что модальное окно ингредиента открывается и закрывается."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()

        main_page.click_ingredient()
        assert main_page.is_modal_open(), "Модальное окно не открылось."

        main_page.close_modal()
        assert not main_page.is_modal_open(), "Модальное окно не закрылось."

    @allure.title("Проверка увеличения счётчика ингредиента при перетаскивании")
    def test_ingredient_counter_increases(self, driver: WebDriver) -> None:
        """Проверяем, что при перетаскивании ингредиента счётчик увеличивается на 1."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()

        initial_count: int = main_page.get_ingredient_count()
        main_page.drag_and_drop_ingredient()
        updated_count: int = main_page.get_ingredient_count()

        assert updated_count == initial_count + 1, "Счётчик ингредиента не увеличился."