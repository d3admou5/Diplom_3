class TestCreateOrder:

    def test_today_orders_counter(self, logged_in_page):
        """Проверка увеличения счётчика 'Выполнено за сегодня' после создания заказа"""
        page = logged_in_page
        counter_before = page.get_order_counter_today()
        page.add_bun_to_constructor()
        page.place_order()
        page.close_modal()
        counter_after = page.get_order_counter_today()
        assert counter_after > counter_before

    def test_total_orders_counter(self, logged_in_page):
        """Проверка увеличения счётчика 'Выполнено за всё время' после создания заказа"""
        page = logged_in_page
        counter_before = page.get_order_counter_total()
        page.add_bun_to_constructor()
        page.place_order()
        page.close_modal()
        counter_after = page.get_order_counter_total()
        assert counter_after > counter_before
