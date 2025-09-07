from web_locators.locators import MainPageLocators, OrderFeedLocators
from web_pages.base_page import BasePage


class MainPage(BasePage):

    def click_constructor_button(self):
        """Переход в 'Конструктор'"""
        self.click(MainPageLocators.CONSTRUCTOR_BTN)
        self.wait_until_element_visibility(MainPageLocators.MAIN_TITLE)

    def click_orders_list_button(self):
        """Переход на страницу 'Лента заказов'"""
        self.move_to_element_and_click(MainPageLocators.ORDERS_LIST_BTN)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)

    def click_on_ingredient(self):
        """Клик по ингредиенту"""
        self.click(MainPageLocators.BUN_CARD)

    def check_show_window_with_details(self):
        """Возвращает текст из окна с деталями ингредиента"""
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def click_cross_button(self):
        """Закрытие окна с деталями ингредиента"""
        self.move_to_element_and_click(MainPageLocators.CLOSE_POPUP_BTN)

    def get_count_value(self):
        """Значение счётчика ингредиента"""
        return int(self.get_text(MainPageLocators.INGREDIENT_COUNT))

    def invisibility_ingredient_details(self):
        """Ожидание, что окно деталей ингредиента исчезнет"""
        self.wait_for_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def check_displayed_ingredient_details(self) -> bool:
        """Проверка, отображается ли окно деталей ингредиента"""
        element = self.find(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return element.is_displayed()

    def add_filling_to_order(self):
        """Перетаскивание ингредиента в заказ"""
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)
