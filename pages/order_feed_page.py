import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    """PageObject для ленты заказов"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Проверяем, отображается ли список заказов")
    def is_orders_list_visible(self) -> bool:
        """Возвращает True, если список заказов отображается"""
        return self.is_visible(OrderFeedPageLocators.ORDERS_LIST)

    @allure.step("Проверяем, отображается ли счётчик 'Выполнено за всё время'")
    def is_total_counter_visible(self) -> bool:
        """Возвращает True, если отображается счётчик 'Выполнено за всё время'"""
        return self.is_visible(OrderFeedPageLocators.TOTAL_COUNTER)

    @allure.step("Проверяем, отображается ли счётчик 'Выполнено за сегодня'")
    def is_today_counter_visible(self) -> bool:
        """Возвращает True, если отображается счётчик 'Выполнено за сегодня'"""
        return self.is_visible(OrderFeedPageLocators.TODAY_COUNTER)

    @allure.step("Открываем первый заказ из ленты")
    def open_first_order(self) -> None:
        """Кликает на первый заказ в списке"""
        self.click(OrderFeedPageLocators.FIRST_ORDER)

    @allure.step("Проверяем, открыто ли модальное окно заказа")
    def is_order_modal_visible(self) -> bool:
        """Возвращает True, если модальное окно заказа отображается"""
        return self.is_visible(OrderFeedPageLocators.ORDER_MODAL)