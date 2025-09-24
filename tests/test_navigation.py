import pytest
import allure
from pages.main_page import MainPage
from locators.urls import Urls


@allure.suite("Тесты навигации")
@pytest.mark.usefixtures("driver")
class TestNavigation:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_constructor_navigation(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        main_page.click_constructor()
        assert driver.current_url == Urls.MAIN_PAGE, "Не удалось перейти на страницу конструктора."

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_feed_orders_navigation(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        main_page.click_feed_orders()
        assert driver.current_url == Urls.FEED_ORDERS_PAGE, "Не удалось перейти на страницу ленты заказов."