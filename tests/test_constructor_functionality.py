import pytest
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage

class TestConstructorFunctionality:

    def test_switch_tabs(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        main_page.open_constructor()
        constructor.switch_to_sauces()
        constructor.switch_to_fillings()
        constructor.switch_to_buns()

    def test_counter_increase(self, driver):
        main_page = MainPage(driver)
        constructor = ConstructorPage(driver)

        main_page.open_constructor()
        before = constructor.get_counter_value()
        constructor.add_first_ingredient()
        after = constructor.get_counter_value()

        assert after > before, "Счетчик ингредиента не увеличился"
