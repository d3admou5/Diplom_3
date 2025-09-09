import allure
from web_pages.base_page import BasePage
from web_locators.locators import LoginPageLocators, MainPageLocators, OrderFeedLocators
from data.config_urls import Urls


class OrderFeedPage(BasePage):

    @allure.step("Логин пользователя с email: {email}")
    def login_user(self, email, password):
        self.open_page(Urls.LOGIN)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.LOGIN_BTN)
        self.find(MainPageLocators.MAIN_TITLE)

    @allure.step("Получение значения счётчика заказов 'Выполнено за сегодня'")
    def get_order_counter_today(self):
        self.open_page(Urls.ORDER_FEED)
        return int(self.get_text(OrderFeedLocators.COUNTER_TODAY))

    @allure.step("Оформление заказа")
    def place_order(self):
        self.move_to_element_and_click(MainPageLocators.ORDER_BTN)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.wait_for_invisibility(OrderFeedLocators.OVERLAY)
        self.move_to_element_and_click(MainPageLocators.MODAL_CLOSE_BTN)

    @allure.step("Получение значения счётчика заказов 'Выполнено за все время'")
    def get_order_counter_total(self):
        self.open_page(Urls.ORDER_FEED)
        return int(self.get_text(OrderFeedLocators.COUNTER_TOTAL))

    @allure.step("Открытие главной страницы конструктора")
    def open_main_page(self):
        self.open_page(Urls.MAIN_URL)

    @allure.step("Перетаскивание ингредиента в заказ")
    def add_filling_to_order(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)

    @allure.step("Добавление булки в конструктор")
    def add_bun_to_constructor(self):
        self.open_page(Urls.MAIN_URL)
        self.drag_and_drop_on_element(MainPageLocators.BUN_CARD, MainPageLocators.ORDER_BASKET)

    @allure.step("Получение номера созданного заказа")
    def get_order_number(self):
        self.wait_for_invisibility(OrderFeedLocators.OVERLAY)
        return self.wait.until(
            lambda d: (text := self.find(MainPageLocators.ORDER_NUMBER).text.strip()).isdigit()
                      and len(text) == 6
                      and text
        )

    @allure.step("Переход в 'Ленту заказов'")
    def go_to_order_feed(self):
        self.open_page(Urls.ORDER_FEED)
        self.wait_until_element_visibility(OrderFeedLocators.ORDERS_LIST_TITLE)

    @allure.step("Получение списка номеров заказов 'В работе'")
    def get_orders_in_progress(self):
        return self.get_elements_text(OrderFeedLocators.NUMBER_IN_PROGRESS)

    @allure.step("Проверка, что заказ {order_number} появился в разделе 'В работе'")
    def is_order_in_work(self, order_number):
        self.find_all(OrderFeedLocators.NUMBER_IN_PROGRESS)
        return self.wait.until(
            lambda d: any(order_number in order for order in self.get_orders_in_progress())
        )
