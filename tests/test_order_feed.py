import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from constants import Urls


@allure.suite("Тесты ленты заказов")
@pytest.mark.usefixtures("driver")
class TestOrderFeed:
    """Набор автотестов для проверки корректности работы раздела 'Лента заказов'."""

    @allure.title("Проверка увеличения счётчика 'Выполнено за всё время'")
    def test_all_time_count_increases(self, driver: WebDriver) -> None:
        """Проверяем, что после оформления заказа счётчик 'Выполнено за всё время' увеличивается на 1."""
        driver.get(Urls.FEED_PAGE)
        feed_page = OrderFeedPage(driver)
        feed_page.wait_for_page_to_load()
        initial_count: int = feed_page.get_all_time_count()

        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        main_page.drag_and_drop_ingredient()
        main_page.click_create_order_button()

        main_page.get_order_number()
        main_page.close_modal()

        main_page.click_feed_orders()
        feed_page.wait_for_page_to_load()

        WebDriverWait(driver, 15).until(
            lambda d: feed_page.get_all_time_count() > initial_count
        )
        updated_count: int = feed_page.get_all_time_count()

        assert updated_count == initial_count + 1, (
            f"Ожидалось: {initial_count + 1}, получено: {updated_count}"
        )

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_appears_in_in_progress_section(self, driver: WebDriver) -> None:
        """Проверяем, что номер нового заказа отображается в разделе 'В работе'."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()
        feed_page = OrderFeedPage(driver)

        main_page.drag_and_drop_ingredient()
        main_page.click_create_order_button()

        order_number_str: str = main_page.get_order_number()
        assert order_number_str.isdigit(), "Номер заказа не найден или имеет неверный формат."
        order_number: int = int(order_number_str)

        main_page.close_modal()
        main_page.click_feed_orders()
        feed_page.wait_for_page_to_load()

        WebDriverWait(driver, 15).until(
            lambda d: order_number in feed_page.get_in_progress_order_numbers()
        )
        in_progress_orders: list[int] = feed_page.get_in_progress_order_numbers()

        assert order_number in in_progress_orders, f"Номер заказа {order_number} не найден в разделе 'В работе'."