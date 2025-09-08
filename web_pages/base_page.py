from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """Базовый класс страницы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        """Найти элемент (ждём его появления в DOM)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Клик по элементу (ждём кликабельности)."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator, strip=True):
        """Получить текст элемента."""
        element = self.find(locator)
        return element.text.strip() if strip else element.text

    def get_current_url(self):
        """Текущий URL."""
        return self.driver.current_url

    def wait_until_element_visibility(self, locator):
        """Ждать, пока элемент станет видимым."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        """Ждать, пока элемент исчезнет/станет невидимым."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_and_drop_on_element(self, locator_one, locator_two):
        """Перетащить элемент на другой элемент."""
        draggable = self.find(locator_one)
        droppable = self.find(locator_two)
        drag_and_drop(self.driver, draggable, droppable)

    def move_to_element_and_click(self, locator):
        """Навести курсор и кликнуть."""
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def open_page(self, url):
        """Открыть url"""
        self.driver.get(url)
