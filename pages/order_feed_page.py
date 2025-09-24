from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderFeedPage(BasePage):
    def get_all_time_count(self):
        count_str = self.get_element_text(OrderLocators.TOTAL_ORDERS_COUNTER[0], OrderLocators.TOTAL_ORDERS_COUNTER[1])
        return int(count_str.replace(',', ''))

    def get_today_count(self):
        count_str = self.get_element_text(OrderLocators.TODAY_ORDERS_COUNTER[0], OrderLocators.TODAY_ORDERS_COUNTER[1])
        return int(count_str)

    def get_in_progress_order_numbers(self):
        self.wait.until(EC.presence_of_all_elements_located(OrderLocators.IN_PROGRESS_ORDERS_LIST))
        elements = self.driver.find_elements(*OrderLocators.IN_PROGRESS_ORDERS_LIST)
        return [int(e.text) for e in elements if e.text.isdigit()]