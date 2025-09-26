import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage
from constants import Urls


@allure.suite("Тесты конструктора")
@pytest.mark.usefixtures("driver")
class TestConstructor:
    """Набор автотестов для проверки работы конструктора бургеров."""

    @allure.title("Проверка открытия модального окна при клике на ингредиент")
    def test_ingredient_modal_opens(self, driver: WebDriver) -> None:
        """Проверяем, что при клике на ингредиент открывается модальное окно."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()

        main_page.click_ingredient()

        assert main_page.is_modal_open(), "Модальное окно не открылось."

    @allure.title("Проверка закрытия модального окна по клику на крестик")
    def test_ingredient_modal_closes(self, driver: WebDriver) -> None:
        """Проверяем, что модальное окно закрывается по клику на кнопку закрытия."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()

        main_page.click_ingredient()
        main_page.close_modal()

        assert not main_page.is_modal_open(), "Модальное окно не закрылось."

    @allure.title("Проверка увеличения счётчика ингредиента при перетаскивании")
    def test_ingredient_counter_increases(self, driver: WebDriver) -> None:
        """Проверяем, что при добавлении ингредиента в корзину счётчик увеличивается на 1."""
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.wait_for_page_to_load()

        initial_count: int = main_page.get_ingredient_count()
        main_page.drag_and_drop_ingredient()
        updated_count: int = main_page.get_ingredient_count()

        assert updated_count == initial_count + 1, "Счётчик ингредиента не увеличился."