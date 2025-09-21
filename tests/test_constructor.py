import pytest
import allure
from pages.main_page import MainPage
from urls import Urls
from locators.main_page_locators import MainPageLocators as Locators
from selenium.common.exceptions import TimeoutException

@allure.suite("Тесты конструктора")
@pytest.mark.usefixtures("driver")
class TestConstructor:
    @allure.title("Проверка открытия модального окна при клике на ингредиент")
    def test_ingredient_modal_opens(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient()
        modal = main_page.find_element(*Locators.MODAL_DETAILS)
        assert modal.is_displayed(), "Модальное окно не открылось."

    @allure.title("Проверка закрытия модального окна по клику на крестик")
    def test_ingredient_modal_closes(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        modal_is_closed = True
        try:
            main_page.find_element(*Locators.MODAL_DETAILS)
            modal_is_closed = False
        except TimeoutException:
            modal_is_closed = True
        assert modal_is_closed, "Модальное окно не закрылось."

    @allure.title("Проверка увеличения счётчика ингредиента при перетаскивании")
    def test_ingredient_counter_increases(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        ingredient = main_page.find_element(*Locators.INGREDIENT)
        initial_count_elements = ingredient.find_elements(*Locators.INGREDIENT_COUNTER)
        initial_count = int(initial_count_elements[0].text) if initial_count_elements else 0
        main_page.drag_and_drop_ingredient()
        updated_count = int(ingredient.find_element(*Locators.INGREDIENT_COUNTER).text)
        assert updated_count == initial_count + 1, "Счетчик ингредиента не увеличился."