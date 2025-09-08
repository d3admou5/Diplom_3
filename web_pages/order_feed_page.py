import time
from selenium.webdriver.support import expected_conditions as EC
from web_pages.base_page import BasePage
from web_locators.locators import LoginPageLocators, MainPageLocators, OrderFeedLocators
from data.config_urls import Urls


class OrderFeedPage(BasePage):

    def login_user(self, email, password):
        """Логин пользователя"""
        self.driver.get(Urls.LOGIN)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BTN)
        self.find(MainPageLocators.MAIN_TITLE)

    def get_order_counter_today(self):
        """Значение счётчика заказов 'Выполнено за сегодня'"""
        self.driver.get(Urls.ORDER_FEED)
        return int(self.get_text(OrderFeedLocators.COUNTER_TODAY))

    def place_order(self):
        """Оформление заказа"""
        self.move_to_element_and_click(MainPageLocators.ORDER_BTN)

    def close_modal(self):
        """Закрытие модального окна"""
        self.wait_for_invisibility(OrderFeedLocators.OVERLAY)
        self.move_to_element_and_click(MainPageLocators.MODAL_CLOSE_BTN)

    def get_order_counter_total(self):
        """Значение счётчика заказов 'Выполнено за все время'"""
        self.driver.get(Urls.ORDER_FEED)
        return int(self.get_text(OrderFeedLocators.COUNTER_TOTAL))

    def open_main_page(self):
        """Открытие главной страницы конструктора"""
        self.driver.get(Urls.MAIN_URL)

    def add_filling_to_order(self):
        """Перетаскивание ингредиента в заказ"""
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)

    def add_bun_to_constructor(self):
        """Открыть главную и перетащить булку в конструктор"""
        self.driver.get(Urls.MAIN_URL)
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)

    def get_order_number(self):
        """Получает номер созданного заказа."""
        self.wait_for_invisibility(OrderFeedLocators.OVERLAY)
        time.sleep(5)
        return self.wait.until(lambda d: (num := d.find_element(*MainPageLocators.ORDER_NUMBER).text.strip()) != "" and num)

    def go_to_order_feed(self):
        """Переход в 'Ленту заказов'"""
        self.driver.get(Urls.ORDER_FEED)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)

    def get_orders_in_progress(self):
        """Возвращает список номеров заказов 'В работе'"""
        return [order.text for order in self.driver.find_elements(*OrderFeedLocators.NUMBER_IN_PROGRESS)]

    def is_order_in_work(self, order_number):
        """Проверка, что заказ появился в списке 'В работе'"""
        self.wait.until(EC.presence_of_all_elements_located(OrderFeedLocators.NUMBER_IN_PROGRESS))

        # теперь ждём, что нужный номер появился в списке
        return self.wait.until(
            lambda d: any(order_number in order for order in self.get_orders_in_progress())
        )
