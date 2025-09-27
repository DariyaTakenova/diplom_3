import allure
from typing import Tuple, Any
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц.
    Содержит универсальные методы для поиска элементов, кликов и работы с ожиданиями.
    """

    def __init__(self, driver: WebDriver, timeout: int = 30) -> None:
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Ожидание видимости элемента: {by}={value}")
    def wait_for_visible(self, by: str, value: str) -> WebElement:
        """Явное ожидание видимости элемента."""
        try:
            return self.wait.until(
                EC.visibility_of_element_located((by, value)),
                message=f"Элемент с локатором '{by}={value}' не был видим после {self.timeout} секунд."
            )
        except TimeoutException as e:
            raise TimeoutException(str(e))

    @allure.step("Ожидание кликабельности элемента: {by}={value}")
    def wait_for_clickable(self, by: str, value: str) -> WebElement:
        """Явное ожидание кликабельности элемента."""
        try:
            return self.wait.until(
                EC.element_to_be_clickable((by, value)),
                message=f"Элемент с локатором '{by}={value}' не был кликабельным после {self.timeout} секунд."
            )
        except TimeoutException as e:
            raise TimeoutException(str(e))

    @allure.step("Клик по элементу: {by}={value}")
    def wait_and_click(self, by: str, value: str) -> None:
        """Ожидание кликабельности и клик по элементу."""
        element = self.wait_for_clickable(by, value)
        element.click()

    @allure.step("Получение текста элемента: {by}={value}")
    def get_element_text(self, by: str, value: str) -> str:
        """Возвращает текст элемента после ожидания его видимости."""
        element = self.wait_for_visible(by, value)
        return element.text.strip()

    @allure.step("Проверка присутствия элемента: {by}={value}")
    def is_element_present(self, by: str, value: str) -> bool:
        """Возвращает True, если элемент присутствует на странице."""
        try:
            self.wait_for_visible(by, value)
            return True
        except TimeoutException:
            return False

    @allure.step(
        "Перетаскивание элемента: {source_locator[0]}={source_locator[1]} → {target_locator[0]}={target_locator[1]}")
    def drag_and_drop_element(self, source_locator: Tuple[str, str], target_locator: Tuple[str, str]) -> None:
        """Перетаскивание элемента с помощью JavaScript (более надёжный способ)."""

        # Явное извлечение By и Value из кортежей для предотвращения KeyError
        source_by, source_value = source_locator
        target_by, target_value = target_locator

        source = self.wait_for_visible(source_by, source_value)
        target = self.wait_for_visible(target_by, target_value)

        try:
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();
                const dragStartEvent = new DragEvent('dragstart', { dataTransfer });
                source.dispatchEvent(dragStartEvent);
                const dropEvent = new DragEvent('drop', { dataTransfer });
                target.dispatchEvent(dropEvent);
                const dragEndEvent = new DragEvent('dragend', { dataTransfer });
                source.dispatchEvent(dragEndEvent);
                """,
                source, target
            )
        except Exception as e:
            raise Exception(
                f"Не удалось выполнить drag-and-drop. Проверьте локаторы или состояние страницы. Ошибка: {e}")

    @allure.step("Ожидание загрузки страницы (проверка наличия <body>)")
    def wait_for_page_to_load(self) -> None:
        """Ожидание загрузки страницы по наличию тега <body>."""
        self.wait.until(
            EC.presence_of_element_located(("tag name", "body")),
            message="Страница не загрузилась корректно."
        )