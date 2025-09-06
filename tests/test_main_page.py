from data.config_urls import Urls


class TestMainPage:

    def test_redirection_to_order_list(self, pages):
        """Проверка перехода на страницу Лента заказов"""
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.ORDERS_FEED

    def test_go_to_constructor(self, pages):
        """Проверка перехода в Конструктор"""
        pages.click_orders_list_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.MAIN_URL

    def test_popup_of_ingredient(self, pages):
        """Проверка появления попапа с деталями ингредиента"""
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    def test_close_ingredient_details_window(self, pages):
        """Проверка закрытия попапа с деталями ингредиента"""
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    def test_ingredient_counter(self, pages):
        """Проверка счетчика ингредиента"""
        prev_counter = pages.get_count_value()
        pages.add_filling_to_order()
        new_counter = pages.get_count_value()
        assert new_counter > prev_counter
