from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_feed_orders(self):
        self.click_element(*Locators.FEED_ORDERS_BUTTON)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click_element(*Locators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click_element(*Locators.INGREDIENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click_element(*Locators.MODAL_CLOSE_BUTTON)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(Locators.INGREDIENT, Locators.BASKET_AREA)

    @allure.step("Создание заказа")
    def make_order(self):
        self.click_element(*Locators.MAKE_ORDER_BUTTON)
        self.wait.until(EC.visibility_of_element_located(Locators.ORDER_NUMBER_POPUP))