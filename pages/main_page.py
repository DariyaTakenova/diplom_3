from pages.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(MainLocators.INGREDIENT, MainLocators.BASKET_AREA)

    def click_create_order_button(self):
        self.wait_and_click(MainLocators.CREATE_ORDER_BUTTON[0], MainLocators.CREATE_ORDER_BUTTON[1])

    def get_order_number(self):
        return self.get_element_text(MainLocators.ORDER_NUMBER_POPUP[0], MainLocators.ORDER_NUMBER_POPUP[1])

    def close_modal(self):
        self.wait_and_click(MainLocators.MODAL_CLOSE_BUTTON[0], MainLocators.MODAL_CLOSE_BUTTON[1])

    def get_ingredient_count(self):
        return int(self.get_element_text(MainLocators.INGREDIENT_COUNTER[0], MainLocators.INGREDIENT_COUNTER[1]))

    def click_ingredient(self):
        self.wait_and_click(MainLocators.INGREDIENT[0], MainLocators.INGREDIENT[1])

    def is_modal_open(self):
        return self.is_element_present(MainLocators.MODAL_DETAILS[0], MainLocators.MODAL_DETAILS[1])

    def click_constructor(self):
        self.wait_and_click(MainLocators.CONSTRUCTOR_BUTTON[0], MainLocators.CONSTRUCTOR_BUTTON[1])

    def click_feed_orders(self):
        self.wait_and_click(MainLocators.FEED_ORDERS_BUTTON[0], MainLocators.FEED_ORDERS_BUTTON[1])