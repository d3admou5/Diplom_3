from web_locators.locators import MainPageLocators, OrdersPageLocators
from web_pages.base_page import BasePage

class MainPage(BasePage):

    def click_constructor_button(self):
        """Переход в 'Конструктор'"""
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BTN)
        self.wait_until_element_visibility(MainPageLocators.MAIN_TITLE)

    def click_orders_list_button(self):
        """Переход на страницу 'Лента заказов'"""
        self.move_to_element_and_click(MainPageLocators.ORDERS_LIST_BTN)
        self.wait_until_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    def click_on_ingredient(self):
        """Кликаем на ингредиент"""
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_CARD)
        self.click_on_element(MainPageLocators.BUN_CARD)

    def check_show_window_with_details(self):
        """Проверяем, что появилось всплывающее окно с деталями ингредиента"""
        self.wait_until_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.get_actually_text(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def click_cross_button(self):
        """Закрываем всплывающее окно крестиком"""
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_COUNT)

    def get_count_value(self):
        """Получаем значение счетчика ингредиента"""
        return int(self.get_actually_text(MainPageLocators.INGREDIENT_COUNT))

    def invisibility_ingredient_details(self):
        """Проверить скрытость деталей ингредиентов"""
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    def check_displayed_ingredient_details(self) -> bool:
        """Проверить наличие окна деталей ингредиентов на экране"""
        return self.check_presence(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    def add_filling_to_order(self):
        """Добавить ингредиент в заказ"""
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_CARD)
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)
