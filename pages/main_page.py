import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):
    """Page Object для главной страницы (конструктор бургеров)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы."""
        super().__init__(driver)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop_ingredient(self) -> None:
        """Перетаскивает первый ингредиент в область корзины."""
        self.drag_and_drop_element(MainLocators.INGREDIENT, MainLocators.BASKET_AREA)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self) -> None:
        """Нажимает на кнопку оформления заказа."""
        self.wait_and_click(*MainLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получение номера заказа из всплывающего окна")
    def get_order_number(self) -> str:
        """Возвращает номер созданного заказа из модального окна."""
        return self.get_element_text(*MainLocators.ORDER_NUMBER_POPUP)

    @allure.step("Закрытие модального окна")
    def close_modal(self) -> None:
        """Закрывает модальное окно заказа или деталей ингредиента."""
        self.wait_and_click(*MainLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение счётчика выбранного ингредиента")
    def get_ingredient_count(self) -> int:
        """Возвращает количество выбранного ингредиента."""
        return int(self.get_element_text(*MainLocators.INGREDIENT_COUNTER))

    @allure.step("Клик по ингредиенту для открытия модального окна")
    def click_ingredient(self) -> None:
        """Открывает карточку ингредиента (модальное окно)."""
        self.wait_and_click(*MainLocators.INGREDIENT)

    @allure.step("Проверка открытия модального окна ингредиента")
    def is_modal_open(self) -> bool:
        """Проверяет, открыто ли модальное окно ингредиента."""
        return self.is_element_present(*MainLocators.MODAL_DETAILS)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self) -> None:
        """Переход на страницу конструктора."""
        self.wait_and_click(*MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_feed_orders(self) -> None:
        """Переход в раздел 'Лента заказов'."""
        self.wait_and_click(*MainLocators.FEED_ORDERS_BUTTON)
