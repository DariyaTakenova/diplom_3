import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.story("Отображение ленты заказов")
    def test_orders_list_is_visible(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            main_page.open_order_feed()

        with allure.step("Проверить, что список заказов отображается"):
            assert order_feed.is_orders_list_visible(), "Лента заказов не отображается"

    @allure.story("Счётчики заказов увеличиваются при новом заказе")
    def test_orders_counters_increase(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            main_page.open_order_feed()

        with allure.step("Запомнить количество выполненных заказов"):
            before = order_feed.get_completed_orders_count()

        with allure.step("Подождать появления нового заказа (или имитировать заказ)"):
            order_feed.wait_for_new_order(before)

        with allure.step("Проверить, что количество заказов увеличилось"):
            after = order_feed.get_completed_orders_count()
            assert after > before, "Счётчик заказов не увеличился"

    @allure.story("Открытие модалки заказа")
    def test_order_modal_window_opens(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Открыть ленту заказов"):
            main_page.open_order_feed()

        with allure.step("Кликнуть на первый заказ в списке"):
            order_feed.click_first_order()

        with allure.step("Проверить, что открылась модалка заказа"):
            assert order_feed.is_order_modal_visible(), "Модальное окно заказа не открылось"
