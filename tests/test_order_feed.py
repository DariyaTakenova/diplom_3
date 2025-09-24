import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.urls import Urls
from selenium.webdriver.support import expected_conditions as EC


@allure.suite("Тесты ленты заказов")
class TestOrderFeed:
    @allure.title("Проверка увеличения счётчика 'Выполнено за всё время'")
    def test_all_time_count_increases(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        feed_page = OrderFeedPage(driver)
        initial_count = feed_page.get_all_time_count()

        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        main_page.click_create_order_button()

        main_page.get_order_number()
        main_page.close_modal()

        main_page.click_feed_orders()
        self.wait.until(lambda d: feed_page.get_all_time_count() > initial_count)
        updated_count = feed_page.get_all_time_count()

        assert updated_count == initial_count + 1, (
            f"Ожидаемый счетчик: {initial_count + 1}, Фактический: {updated_count}"
        )

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_appears_in_in_progress_section(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        feed_page = OrderFeedPage(driver)

        main_page.drag_and_drop_ingredient()
        main_page.click_create_order_button()

        order_number_str = main_page.get_order_number()
        assert order_number_str.isdigit(), "Номер заказа не был найден или не является числом"
        order_number = int(order_number_str)

        main_page.close_modal()
        main_page.click_feed_orders()

        in_progress_orders = feed_page.get_in_progress_order_numbers()
        self.wait.until(lambda d: order_number in feed_page.get_in_progress_order_numbers())

        assert order_number in in_progress_orders, f"Номер заказа {order_number} не найден в разделе 'В работе'."