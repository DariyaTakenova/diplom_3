import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    """PageObject для конструктора бургеров"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    @allure.step("Переключаемся на вкладку 'Булки'")
    def switch_to_buns(self) -> None:
        """Кликает по вкладке 'Булки'"""
        self.click(ConstructorPageLocators.BUNS_TAB)

    @allure.step("Переключаемся на вкладку 'Соусы'")
    def switch_to_sauces(self) -> None:
        """Кликает по вкладке 'Соусы'"""
        self.click(ConstructorPageLocators.SAUCES_TAB)

    @allure.step("Переключаемся на вкладку 'Начинки'")
    def switch_to_fillings(self) -> None:
        """Кликает по вкладке 'Начинки'"""
        self.click(ConstructorPageLocators.FILLINGS_TAB)

    @allure.step("Получаем значение счётчика ингредиента")
    def get_counter_value(self) -> int:
        """Возвращает текущее значение счётчика ингредиента"""
        text = self.get_text(ConstructorPageLocators.COUNTER)
        return int(text) if text.isdigit() else 0

    @allure.step("Добавляем первый ингредиент в конструктор")
    def add_first_ingredient(self) -> None:
        """Перетаскивает первый ингредиент в конструктор"""
        ingredient = self.wait_for_visible(ConstructorPageLocators.FIRST_INGREDIENT)
        target = self.wait_for_visible(ConstructorPageLocators.CONSTRUCTOR_AREA)
        self.actions.drag_and_drop(ingredient, target).perform()

    @allure.step("Нажимаем кнопку 'Оформить заказ'")
    def click_place_order(self) -> None:
        """Кликает по кнопке оформления заказа"""
        self.click(ConstructorPageLocators.PLACE_ORDER_BUTTON)