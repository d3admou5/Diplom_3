from data.config_urls import Urls
from web_pages.main_page import MainPage

class TestMainPage:

    def test_redirection_to_order_list(self, driver_do):
        """Проверка перехода на страницу Лента заказов"""
        pages = MainPage(driver_do)
        pages.click_orders_list_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.ORDER_FEED

    def test_go_to_constructor(self, driver_do):
        """Проверка перехода в Конструктор"""
        pages = MainPage(driver_do)
        pages.click_orders_list_button()
        pages.click_constructor_button()
        current_url = pages.get_current_url()
        assert current_url == Urls.MAIN_URL

    def test_popup_of_ingredient(self, driver_do):
        """Проверка появления попапа с деталями ингредиента"""
        pages = MainPage(driver_do)
        pages.click_on_ingredient()
        actually_text = pages.check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    def test_close_ingredient_details_window(self, driver_do):
        """Проверка закрытия попапа с деталями ингредиента"""
        pages = MainPage(driver_do)
        pages.click_on_ingredient()
        pages.click_cross_button()
        pages.invisibility_ingredient_details()
        assert pages.check_displayed_ingredient_details() == False

    def test_ingredient_counter(self, driver_do):
        """Проверка счетчика ингредиента"""
        pages = MainPage(driver_do)
        prev_counter = pages.get_count_value()
        pages.add_filling_to_order()
        new_counter = pages.get_count_value()
        assert new_counter > prev_counter
