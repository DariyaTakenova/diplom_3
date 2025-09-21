from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators as Locators
from data import Data
from selenium.webdriver.common.by import By
import allure

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Получение счётчика 'Выполнено за всё время'")
    def get_all_time_count(self):
        # Используем локатор из data.py
        all_time_count_locator = (By.XPATH, f".//p[text()='{Data.ORDERS_TOTAL_TEXT}']/following-sibling::p")
        count_element = self.find_element(*all_time_count_locator)
        return int(count_element.text.replace(',', ''))

    @allure.step("Получение счётчика 'Выполнено за сегодня'")
    def get_today_count(self):
        # Используем локатор из data.py
        today_count_locator = (By.XPATH, f".//p[text()='{Data.ORDERS_TODAY_TEXT}']/following-sibling::p")
        count_element = self.find_element(*today_count_locator)
        return int(count_element.text)

    @allure.step("Получение последнего номера заказа в разделе 'В работе'")
    def get_last_order_in_progress(self):
        order_list = self.find_element(*Locators.ORDER_LIST_IN_PROGRESS)
        if order_list:
            orders = order_list.find_elements(*Locators.ORDER_NUMBER_IN_PROGRESS)
            return int(orders[0].text) if orders else None
        return None