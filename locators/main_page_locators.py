from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    FEED_ORDERS_BUTTON = (By.XPATH, ".//p[text()='Лента заказов']")
    INGREDIENT = (By.CSS_SELECTOR, "li[class*='BurgerIngredient_ingredient__'] a")
    MODAL_DETAILS = (By.CSS_SELECTOR, "div[class*='Modal_modal_opened__']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[@class='Counter_counter__num']")
    BASKET_AREA = (By.CSS_SELECTOR, "div[class*='BurgerConstructor_burger__list']")
    TOTAL_PRICE = (By.XPATH, ".//p[contains(@class, 'total')]/../..//p[@class='digits-default']")
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUMBER_POPUP = (By.CSS_SELECTOR, "h2.Modal_modal__title_3F6X_")