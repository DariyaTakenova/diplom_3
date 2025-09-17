import pytest
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:

    def test_order_counters(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        main_page.open_order_feed()
        assert order_feed.is_orders_list_visible(), "Лента заказов не отображается"
