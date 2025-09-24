from selenium.webdriver.common.by import By


class MainLocators:
    """Класс с локаторами для главной страницы."""
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_ORDERS_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")
    INGREDIENT = (By.CSS_SELECTOR, "li[class*='BurgerIngredient_ingredient__'] a")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'Counter_counter__num')]")
    MODAL_DETAILS = (By.CSS_SELECTOR, "div[class*='Modal_modal__content']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    BASKET_AREA = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_burgerConstructor__']")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUMBER_POPUP = (By.CSS_SELECTOR, "div[class*='Modal_modal_'] h2[class*='Modal_modal__title']")