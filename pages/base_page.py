import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=20):  # Увеличен таймаут
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, by, value):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, value)))
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором '{by}={value}' не был видим после ожидания.") from e

    def wait_for_page_to_load(self):
        """Ждёт, пока основной контент страницы загрузится и станет видимым."""
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    def drag_and_drop_element(self, source_locator, target_locator):
        retries = 3
        for i in range(retries):
            try:
                source_element = self.wait.until(EC.element_to_be_clickable(source_locator))
                target_element = self.wait.until(EC.visibility_of_element_located(target_locator))
                actions = ActionChains(self.driver)
                # Добавлено короткое ожидание для предотвращения "Stale Element"
                actions.drag_and_drop(source_element, target_element).perform()
                return True
            except (TimeoutException, StaleElementReferenceException) as e:
                print(f"Попытка {i+1} из {retries} не удалась. Перезапуск...")
                if i == retries - 1:
                    raise Exception(f"Не удалось выполнить drag-and-drop. Проверьте локаторы или состояние страницы. Ошибка: {e}")
                time.sleep(2)

    def get_element_text(self, by, value):
        element = self.find_element(by, value)
        return element.text

    def wait_and_click(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except TimeoutException as e:
            raise TimeoutException(f"Элемент с локатором '{by}={value}' не был кликабельным после ожидания.") from e

    def is_element_present(self, by, value):
        try:
            self.wait.until(EC.presence_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def is_modal_open(self):
        from locators.main_page_locators import MainLocators
        return self.is_element_present(MainLocators.MODAL_DETAILS[0], MainLocators.MODAL_DETAILS[1])