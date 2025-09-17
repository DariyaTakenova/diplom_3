from pages.base_page import BasePage
from locators import ConstructorPageLocators

class ConstructorPage(BasePage):
    # Переключение на вкладку "Булки"
    def switch_to_buns(self):
        self.click(ConstructorPageLocators.BUNS_TAB)

    # Переключение на вкладку "Соусы"
    def switch_to_sauces(self):
        self.click(ConstructorPageLocators.SAUCES_TAB)

    # Переключение на вкладку "Начинки"
    def switch_to_fillings(self):
        self.click(ConstructorPageLocators.FILLINGS_TAB)

    # Добавить первый ингредиент из списка
    def add_first_ingredient(self):
        self.click(ConstructorPageLocators.FIRST_INGREDIENT)

    # Получить значение счетчика ингредиента
    def get_counter_value(self):
        try:
            return int(self.get_text(ConstructorPageLocators.COUNTER))
        except:
            return 0
