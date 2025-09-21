import allure
from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех PageObject"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Клик по элементу {locator}")
    def click(self, locator: Tuple[str, str]) -> None:
        """Ожидание кликабельности и клик по элементу"""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
        element.click()

    @allure.step("Ввод текста в элемент {locator}")
    def input_text(self, locator: Tuple[str, str], text: str) -> None:
        """Ожидание видимости поля, очистка и ввод текста"""
        element: WebElement = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден для ввода текста"
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента {locator}")
    def get_text(self, locator: Tuple[str, str]) -> str:
        """Ожидание видимости и возврат текста элемента"""
        element: WebElement = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден для получения текста"
        )
        return element.text

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_for_visible(self, locator: Tuple[str, str]) -> WebElement:
        """Ожидает, что элемент появится на странице"""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Проверка, отображается ли элемент {locator}")
    def is_visible(self, locator: Tuple[str, str]) -> bool:
        """Возвращает True, если элемент отображается"""
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator),
                message=f"Элемент {locator} не отображается"
            )
            return True
        except Exception:
            return False