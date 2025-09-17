from pages.base_page import BasePage
from locators import OrderFeedLocators

class OrderFeedPage(BasePage):
    # Проверка отображения списка заказов
    def is_orders_list_visible(self):
        return self.is_visible(OrderFeedLocators.ORDERS_LIST)
