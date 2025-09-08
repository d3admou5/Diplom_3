import allure
from data.config_urls import Urls
from web_pages.main_page import MainPage


class TestMainPage:

    @allure.feature("Переходы по страницам")
    @allure.story("Проверка перехода на страницу Лента заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_redirection_to_order_list(self, driver_do):
        pages = MainPage(driver_do)
        with allure.step("Нажатие кнопки 'Лента заказов'"):
            pages.click_orders_list_button()
        with allure.step("Проверка текущего URL"):
            current_url = pages.get_current_url()
            assert current_url == Urls.ORDER_FEED

    @allure.feature("Переходы по страницам")
    @allure.story("Проверка перехода в Конструктор")
    def test_go_to_constructor(self, driver_do):
        pages = MainPage(driver_do)
        with allure.step("Переход на 'Лента заказов'"):
            pages.click_orders_list_button()
        with allure.step("Переход в 'Конструктор'"):
            pages.click_constructor_button()
        with allure.step("Проверка текущего URL"):
            current_url = pages.get_current_url()
            assert current_url == Urls.MAIN_URL

    @allure.feature("Интерфейс ингредиентов")
    @allure.story("Проверка появления попапа с деталями ингредиента")
    def test_popup_of_ingredient(self, driver_do):
        pages = MainPage(driver_do)
        with allure.step("Клик по ингредиенту"):
            pages.click_on_ingredient()
        with allure.step("Получение текста из попапа"):
            actually_text = pages.check_show_window_with_details()
            assert actually_text == "Детали ингредиента"

    @allure.feature("Интерфейс ингредиентов")
    @allure.story("Проверка закрытия попапа с деталями ингредиента")
    def test_close_ingredient_details_window(self, driver_do):
        pages = MainPage(driver_do)
        with allure.step("Клик по ингредиенту"):
            pages.click_on_ingredient()
        with allure.step("Закрытие окна деталей ингредиента"):
            pages.click_cross_button()
            pages.invisibility_ingredient_details()
        with allure.step("Проверка, что окно закрылось"):
            assert pages.check_displayed_ingredient_details() == False

    @allure.feature("Интерфейс ингредиентов")
    @allure.story("Проверка счетчика ингредиента")
    def test_ingredient_counter(self, driver_do):
        pages = MainPage(driver_do)
        with allure.step("Получение текущего значения счетчика"):
            prev_counter = pages.get_count_value()
        with allure.step("Добавление ингредиента в заказ"):
            pages.add_filling_to_order()
        with allure.step("Проверка, что счетчик увеличился"):
            new_counter = pages.get_count_value()
            assert new_counter > prev_counter
