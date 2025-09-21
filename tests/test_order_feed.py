import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from urls import Urls
from locators.main_page_locators import MainPageLocators as Locators
from locators.order_feed_page_locators import OrderFeedPageLocators as OrderLocators


@allure.suite("Тесты ленты заказов")
@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    @allure.title("Проверка, что при создании заказа увеличивается счётчик 'Выполнено за всё время'")
    def test_all_time_count_increases(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_all_time_count()

        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        main_page.make_order()

        driver.get(Urls.FEED_ORDERS_PAGE)
        updated_count = order_feed_page.get_all_time_count()
        assert updated_count > initial_count, "Счётчик 'Выполнено за всё время' не увеличился."

    @allure.title("Проверка, что при создании заказа увеличивается счётчик 'Выполнено за сегодня'")
    def test_today_count_increases(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        order_feed_page = OrderFeedPage(driver)
        initial_count = order_feed_page.get_today_count()

        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        main_page.make_order()

        driver.get(Urls.FEED_ORDERS_PAGE)
        updated_count = order_feed_page.get_today_count()
        assert updated_count > initial_count, "Счётчик 'Выполнено за сегодня' не увеличился."

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе 'В работе'")
    def test_order_number_appears_in_in_progress_section(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        main_page.make_order()

        order_number_text = main_page.find_element(*Locators.ORDER_NUMBER_POPUP).text
        order_number = int(order_number_text)

        driver.get(Urls.FEED_ORDERS_PAGE)
        order_feed_page = OrderFeedPage(driver)
        last_order_in_progress = order_feed_page.get_last_order_in_progress()

        assert last_order_in_progress == order_number, "Номер заказа не появился в разделе 'В работе'."