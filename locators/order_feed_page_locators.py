from selenium.webdriver.common.by import By


class OrderLocators:
    """Локаторы для страницы 'Лента заказов'."""

    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    IN_PROGRESS_ORDERS_LIST = (By.XPATH, "//p[text()='В работе']/../ul/li/p")

    ORDER_NUMBER_IN_FEED = (By.XPATH, "//ul[contains(@class,'OrderFeed_ordersList')]//a/div/p")
