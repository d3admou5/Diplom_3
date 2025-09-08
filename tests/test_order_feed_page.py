import allure

class TestCreateOrder:

    @allure.feature("Счётчики заказов")
    @allure.story("Проверка увеличения счётчика 'Выполнено за сегодня'")
    def test_today_orders_counter(self, logged_in_page):
        page = logged_in_page
        with allure.step("Получаем текущее значение счётчика 'Выполнено за сегодня'"):
            counter_before = page.get_order_counter_today()
        with allure.step("Добавляем булку в конструктор"):
            page.add_bun_to_constructor()
        with allure.step("Оформляем заказ"):
            page.place_order()
        with allure.step("Закрываем модальное окно"):
            page.close_modal()
        with allure.step("Получаем новое значение счётчика 'Выполнено за сегодня'"):
            counter_after = page.get_order_counter_today()
        with allure.step("Проверяем, что счётчик увеличился"):
            assert counter_after > counter_before

    @allure.feature("Счётчики заказов")
    @allure.story("Проверка увеличения счётчика 'Выполнено за всё время'")
    def test_total_orders_counter(self, logged_in_page):
        page = logged_in_page
        with allure.step("Получаем текущее значение счётчика 'Выполнено за всё время'"):
            counter_before = page.get_order_counter_total()
        with allure.step("Добавляем булку в конструктор"):
            page.add_bun_to_constructor()
        with allure.step("Оформляем заказ"):
            page.place_order()
        with allure.step("Закрываем модальное окно"):
            page.close_modal()
        with allure.step("Получаем новое значение счётчика 'Выполнено за всё время'"):
            counter_after = page.get_order_counter_total()
        with allure.step("Проверяем, что счётчик увеличился"):
            assert counter_after > counter_before

    @allure.feature("Создание заказа")
    @allure.story("Проверка появления созданного заказа в разделе 'В работе'")
    def test_new_order_appears_in_work_list(self, logged_in_page):
        page = logged_in_page
        with allure.step("Добавляем булку в конструктор"):
            page.add_bun_to_constructor()
        with allure.step("Оформляем заказ"):
            page.place_order()
        with allure.step("Получаем номер созданного заказа"):
            order_number = page.get_order_number()
        with allure.step("Закрываем модальное окно"):
            page.close_modal()
        with allure.step("Переходим в 'Ленту заказов'"):
            page.go_to_order_feed()
        with allure.step("Проверяем, что заказ появился в разделе 'В работе'"):
            assert page.is_order_in_work(order_number)
