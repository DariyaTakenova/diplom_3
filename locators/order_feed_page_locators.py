from selenium.webdriver.common.by import By


class OrderLocators:
    """Класс с локаторами для страницы 'Лента заказов'."""
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/../p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/../p")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//p[text()='В работе']/../ul/li/p")
    ORDER_NUMBER_IN_FEED = (By.XPATH, "//div[contains(@class, 'OrderFeed_ordersList_')]//a/div/p")