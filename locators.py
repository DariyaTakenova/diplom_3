from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")


class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")


class RegisterPageLocators:
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Личный Кабинет']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    FIRST_INGREDIENT = (By.XPATH, "//div[@class='BurgerIngredient_ingredient__1TVf6'][1]")
    COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    CONSTRUCTOR_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class OrderFeedPageLocators:
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_list__')]/li")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    FIRST_ORDER = (By.XPATH, "(//ul[contains(@class,'OrderFeed_list__')]/li)[1]")
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__2jX1h")