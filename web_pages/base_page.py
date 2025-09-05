from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """Инициализация класса."""
        self.driver = driver

    def click_on_element(self, locator):
        """Кликаем по элементу"""
        self.driver.find_element(*locator).click()

    def wait_until_element_visibility(self, locator):
        """Дождаться видимости элемента"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Ожидание, что элемент станет кликабельным"""
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))

    def get_actually_text(self, locator):
        """Получить текущий текст"""
        return self.driver.find_element(*locator).text

    def get_current_url(self):
        """Получить текущую ссылку"""
        return self.driver.current_url

    def check_invisibility(self, locator) -> object:
        """Проверить что элемент невидим"""
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    def check_presence(self, locator):
        """Проверить присутствие элемента на странице"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def drag_and_drop_on_element(self, locator_one, locator_two):
        """Перетащить элемент"""
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()

    def move_to_element_and_click(self, locator):
        """Переместиться до элемента и кликнуть"""
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
