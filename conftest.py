import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    """
    Фикстура для запуска браузеров Chrome и Firefox.
    Окно всегда разворачивается на полный экран для корректного взаимодействия с элементами.
    """
    browser_name = request.param

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    try:
        driver.maximize_window()
    except Exception:
        pass

    yield driver
    driver.quit()
