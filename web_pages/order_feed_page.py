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

    def add_bun_to_constructor(self):
        """Добавление булки в конструктор"""
        self.driver.get(Urls.MAIN_URL)
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BTN)

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

    def create_order(self):
        """Создание заказа (булка → оформить → закрыть модалку)"""
        self.add_bun_to_constructor()
        self.place_order()
        self.close_modal()
