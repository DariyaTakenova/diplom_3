from selenium.webdriver.common.by import By


class MainLocators:
    """Локаторы для главной страницы (конструктор)."""

    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_ORDERS_BUTTON = (By.XPATH, "//p[text()='Лента заказов']")

    # Ингредиенты
    INGREDIENT = (By.CSS_SELECTOR, "ul li a[class*='BurgerIngredient_ingredient__']")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class*='Counter_counter__num']")

    # Модальное окно ингредиента
    MODAL_DETAILS = (By.CSS_SELECTOR, "div[class*='Modal_modal__content']")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")

    # Корзина
    BASKET_AREA = (By.CSS_SELECTOR, "section[class*='BurgerConstructor_burgerConstructor__']")
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Попап с номером заказа
    ORDER_NUMBER_POPUP = (By.CSS_SELECTOR, "div[class*='Modal_modal__'] h2[class*='Modal_modal__title']")
