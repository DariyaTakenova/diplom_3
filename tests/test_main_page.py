import pytest
import allure
from pages.main_page import MainPage
from locators.urls import Urls

@pytest.mark.usefixtures("driver")
@allure.suite("Тесты главной страницы")
class TestMainPage:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_constructor_navigation(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert driver.current_url == Urls.MAIN_PAGE, "Не удалось перейти на страницу конструктора."

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_feed_orders_navigation(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_feed_orders()
        assert driver.current_url == Urls.FEED_ORDERS_PAGE, "Не удалось перейти на страницу ленты заказов."

    @allure.title("Проверка открытия и закрытия модального окна ингредиента")
    def test_ingredient_modal(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.is_modal_open(), "Модальное окно не открылось."
        main_page.close_modal()
        assert not main_page.is_modal_open(), "Модальное окно не закрылось."

    @allure.title("Проверка увеличения счётчика ингредиента при перетаскивании")
    def test_ingredient_counter_increases(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        initial_count = main_page.get_ingredient_count()
        main_page.drag_and_drop_ingredient()
        updated_count = main_page.get_ingredient_count()
        assert updated_count == initial_count + 1, "Счетчик ингредиента не увеличился."
