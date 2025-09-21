import pytest
from selenium import webdriver

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()