from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, by, value):
        return self.wait.until(EC.visibility_of_element_located((by, value)))

    def click_element(self, by, value):
        self.wait.until(EC.element_to_be_clickable((by, value))).click()

    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element(*source_locator)
        target_element = self.find_element(*target_locator)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()