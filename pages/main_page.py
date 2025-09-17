from pages.base_page import BasePage
from locators import MainPageLocators

class MainPage(BasePage):
    # Открыть раздел "Конструктор"
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    # Открыть раздел "Лента заказов"
    def open_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_TAB)

    # Нажать кнопку входа в аккаунт
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)
