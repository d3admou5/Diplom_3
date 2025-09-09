import allure
from web_locators.locators import MainPageLocators, OrderFeedLocators
from web_pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Переход в 'Конструктор'")
    def click_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BTN)
        self.wait_until_element_visibility(MainPageLocators.MAIN_TITLE)

    @allure.step("Переход на страницу 'Лента заказов'")
    def click_orders_list_button(self):
        self.move_to_element_and_click(MainPageLocators.ORDERS_LIST_BTN)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click(MainPageLocators.BUN_CARD)

    @allure.step("Получение текста из окна с деталями ингредиента")
    def check_show_window_with_details(self):
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step("Закрытие окна с деталями ингредиента")
    def click_cross_button(self):
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_BTN)

    @allure.step("Получение значения счётчика ингредиента")
    def get_count_value(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNT))

    @allure.step("Ожидание исчезновения окна деталей ингредиента")
    def invisibility_ingredient_details(self):
        self.wait_for_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step("Проверка, отображается ли окно деталей ингредиента")
    def check_displayed_ingredient_details(self) -> bool:
        element = self.find(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return element.is_displayed()

    @allure.step("Перетаскивание ингредиента в заказ")
    def add_filling_to_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)
