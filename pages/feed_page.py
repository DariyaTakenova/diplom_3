import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class FeedPage(BasePage):
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/../p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/../p")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//p[text()='В работе']/../ul/li")

    @allure.step('Получение значения счетчика "Выполнено за всё время"')
    def get_total_orders_count(self):
        return self.find_element(*self.TOTAL_ORDERS_COUNTER).text

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_today_orders_count(self):
        return self.find_element(*self.TODAY_ORDERS_COUNTER).text

    @allure.step('Получение списка номеров заказов "В работе"')
    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*self.IN_PROGRESS_ORDERS_LIST)
        return [elem.text for elem in elements]