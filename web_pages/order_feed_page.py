from selenium.webdriver.support import expected_conditions as EC
from web_pages.base_page import BasePage
from web_locators.locators import LoginPageLocators, MainPageLocators, OrderFeedLocators
from seletools.actions import drag_and_drop


class OrderFeedPage(BasePage):
    def login_user(self, email, password, login_url):
        """Логин пользователя"""
        self.driver.get(login_url)
        self.wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BTN)).click()
        self.wait.until(EC.presence_of_element_located(MainPageLocators.MAIN_TITLE))

    def get_order_counter_today(self, order_feed_url):
        """Получаем значение счётчика заказов 'Выполнено за сегодня'"""
        self.driver.get(order_feed_url)
        counter_element = self.wait.until(EC.presence_of_element_located(OrderFeedLocators.COUNTER_TODAY))
        return int(counter_element.text)

    def add_bun_to_constructor(self, constructor_url):
        """Добавляем булку в конструктор"""
        self.driver.get(constructor_url)
        bun = self.wait.until(EC.presence_of_element_located(MainPageLocators.BUN_CARD))
        drop_area = self.driver.find_element(*MainPageLocators.ORDER_BTN)
        drag_and_drop(self.driver, bun, drop_area)

    def place_order(self):
        """Оформляем заказ"""
        order_btn_locator = MainPageLocators.ORDER_BTN
        self.move_to_element_and_click(order_btn_locator)

    def close_modal(self):
        """Закрываем модальное окно"""
        overlay_locator = OrderFeedLocators.OVERLAY
        modal_close_locator = MainPageLocators.MODAL_CLOSE_BTN
        self.wait.until(EC.invisibility_of_element_located(overlay_locator))
        self.move_to_element_and_click(modal_close_locator)

    def get_order_counter_total(self, order_feed_url):
        """Получаем значение счётчика заказов 'Выполнено за все время'"""
        self.driver.get(order_feed_url)
        counter_element = self.wait.until(EC.presence_of_element_located(OrderFeedLocators.COUNTER_TOTAL))
        return int(counter_element.text)

    def create_order(self, main_url):
        """Добавляем булку в конструктор, оформляем заказ и закрываем модалку"""
        self.add_bun_to_constructor(main_url)
        self.place_order()
        self.close_modal()