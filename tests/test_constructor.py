# tests/test_constructor.py

import allure
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from data import Data


@allure.feature("Конструктор бургеров")
class TestConstructor:

    @allure.story("Переключение на вкладку 'Соусы'")
    def test_switch_to_sauces_tab(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open_constructor()

        with allure.step("Переключиться на вкладку 'Соусы'"):
            constructor.switch_to_sauces()

        with allure.step("Проверить, что вкладка 'Соусы' активна"):
            assert constructor.is_sauces_tab_active(), "Вкладка 'Соусы' не активна"

    @allure.story("Переключение на вкладку 'Начинки'")
    def test_switch_to_fillings_tab(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open_constructor()

        with allure.step("Переключиться на вкладку 'Начинки'"):
            constructor.switch_to_fillings()

        with allure.step("Проверить, что вкладка 'Начинки' активна"):
            assert constructor.is_fillings_tab_active(), "Вкладка 'Начинки' не активна"

    @allure.story("Переключение на вкладку 'Булки'")
    def test_switch_to_buns_tab(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open_constructor()

        with allure.step("Переключиться на вкладку 'Булки'"):
            constructor.switch_to_buns()

        with allure.step("Проверить, что вкладка 'Булки' активна"):
            assert constructor.is_buns_tab_active(), "Вкладка 'Булки' не активна"

    @allure.story("Увеличение счётчика ингредиента при добавлении")
    def test_counter_increase_after_adding_ingredient(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open_constructor()

        with allure.step("Запомнить текущее значение счётчика у первого ингредиента"):
            before = constructor.get_first_ingredient_counter()

        with allure.step("Добавить первый ингредиент в бургер"):
            constructor.add_first_ingredient()

        with allure.step("Проверить, что счётчик увеличился"):
            after = constructor.get_first_ingredient_counter()
            assert after > before, "Счётчик ингредиента не увеличился"

    @allure.story("Удаление ингредиента уменьшает счётчик")
    def test_counter_decrease_after_removing_ingredient(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        with allure.step("Открыть конструктор"):
            main_page.open_constructor()

        with allure.step("Добавить первый ингредиент"):
            constructor.add_first_ingredient()
            before = constructor.get_first_ingredient_counter()

        with allure.step("Удалить ингредиент из бургера"):
            constructor.remove_first_ingredient()

        with allure.step("Проверить, что счётчик уменьшился"):
            after = constructor.get_first_ingredient_counter()
            assert after < before, "Счётчик ингредиента не уменьшился"
