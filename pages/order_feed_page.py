import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderLocators


class OrderFeedPage(BasePage):
    """Page Object для страницы 'Лента заказов'."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы."""
        super().__init__(driver)

    @allure.step("Получение общего количества заказов за всё время")
    def get_all_time_count(self) -> int:
        """Возвращает общее количество всех заказов за всё время."""
        count_str: str = self.get_element_text(*OrderLocators.TOTAL_ORDERS_COUNTER)
        return int(count_str.replace(',', ''))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_count(self) -> int:
        """Возвращает количество заказов за текущий день."""
        count_str: str = self.get_element_text(*OrderLocators.TODAY_ORDERS_COUNTER)
        return int(count_str)

    @allure.step("Получение списка номеров заказов, находящихся в работе")
    def get_in_progress_order_numbers(self) -> list[int]:
        """Возвращает список номеров заказов, которые находятся в работе."""
        self.wait.until(EC.presence_of_all_elements_located(OrderLocators.IN_PROGRESS_ORDERS_LIST))
        elements = self.driver.find_elements(*OrderLocators.IN_PROGRESS_ORDERS_LIST)
        return [int(e.text) for e in elements if e.text.isdigit()]
