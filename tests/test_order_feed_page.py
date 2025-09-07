from data.config_urls import Urls


class TestCreateOrder:

    def test_today_orders_counter(self, logged_in_page):
        """Проверка увеличения счётчика 'Выполнено за сегодня' после создания заказа"""
        page = logged_in_page
        counter_before = page.get_order_counter_today(Urls.ORDER_FEED)
        page.create_order(Urls.MAIN_URL)
        counter_after = page.get_order_counter_today(Urls.ORDER_FEED)
        assert counter_after > counter_before

    def test_total_orders_counter(self, logged_in_page):
        """Проверка увеличения счётчика 'Выполнено за всё время' после создания заказа"""
        page = logged_in_page
        counter_before = page.get_order_counter_total(Urls.ORDER_FEED)
        page.create_order(Urls.MAIN_URL)
        counter_after = page.get_order_counter_total(Urls.ORDER_FEED)
        assert counter_after > counter_before
