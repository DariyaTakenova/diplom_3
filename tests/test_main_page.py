import pytest
import allure
from pages.main_page import MainPage
from urls import Urls
from locators.main_page_locators import MainPageLocators as Locators


@pytest.mark.usefixtures("driver")
class TestMainPage:
    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_constructor_navigation(self, driver):
        driver.get(Urls.FEED_ORDERS_PAGE)
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert driver.current_url == Urls.MAIN_PAGE, "Не удалось перейти на страницу конструктора."

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_feed_orders_navigation(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_feed_orders()
        assert driver.current_url == Urls.FEED_ORDERS_PAGE, "Не удалось перейти на страницу ленты заказов."

    @allure.title("Проверка открытия модального окна при клике на ингредиент")
    def test_ingredient_modal_opens(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient()
        modal = main_page.find_element(*Locators.MODAL_DETAILS)  # Исправлено
        assert modal is not None, "Модальное окно не открылось."
        assert modal.is_displayed(), "Модальное окно не отображается."

    @allure.title("Проверка закрытия модального окна по клику на крестик")
    def test_ingredient_modal_closes(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_modal()
        # Проверка, что элемент не найден после закрытия
        try:
            main_page.find_element(*Locators.MODAL_DETAILS)
            is_modal_closed = False
        except TimeoutException:
            is_modal_closed = True

        assert is_modal_closed, "Модальное окно не закрылось."

    @allure.title("Проверка увеличения счётчика ингредиента при перетаскивании")
    def test_ingredient_counter_increases(self, driver):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        ingredient = main_page.find_element(*Locators.INGREDIENT)  # Исправлено
        initial_count_text = ingredient.find_element(*Locators.INGREDIENT_COUNTER).text
        initial_count = int(initial_count_text) if initial_count_text else 0
        main_page.drag_and_drop_ingredient()
        updated_count = int(ingredient.find_element(*Locators.INGREDIENT_COUNTER).text)
        assert updated_count == initial_count + 1, "Счетчик ингредиента не увеличился."