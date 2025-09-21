from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ALL_TIME_COUNT = (By.XPATH, ".//p[text()='Выполнено за всё время']/following-sibling::p")
    TODAY_COUNT = (By.XPATH, ".//p[text()='Выполнено за сегодня']/following-sibling::p")
    ORDER_LIST_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_ordersListReady__')]")
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_ordersListReady__')]//li/a")