from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FIRST_INGREDIENT = (By.XPATH, "//section//ul/li[1]")
    COUNTER = (By.CSS_SELECTOR, "p.Counter_counter__num__3nue1")

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

class ProfilePageLocators:
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")

class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDERS_LIST = (By.CSS_SELECTOR, "ul.OrderFeed_list__YjK-Q")
