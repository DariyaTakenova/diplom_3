import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1280,800")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=800")
        driver = webdriver.Firefox(options=options)

    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
