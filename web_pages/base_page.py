import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """Базовый класс страницы."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Поиск элемента {locator}")
    def find(self, locator):
        """Найти элемент (ждём его появления в DOM)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        """Клик по элементу (ждём кликабельности)."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator, strip=True):
        """Получить текст элемента."""
        element = self.find(locator)
        return element.text.strip() if strip else element.text

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        """Текущий URL."""
        return self.driver.current_url

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_until_element_visibility(self, locator):
        """Ждать, пока элемент станет видимым."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator):
        """Ждать, пока элемент исчезнет/станет невидимым."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетаскивание элемента {locator_one} на {locator_two}")
    def drag_and_drop_on_element(self, locator_one, locator_two):
        """Перетащить элемент на другой элемент."""
        draggable = self.find(locator_one)
        droppable = self.find(locator_two)
        drag_and_drop(self.driver, draggable, droppable)

    @allure.step("Наведение на элемент {locator} и клик")
    def move_to_element_and_click(self, locator):
        """Навести курсор и кликнуть."""
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step("Открытие страницы {url}")
    def open_page(self, url):
        """Открыть url"""
        self.driver.get(url)

    @allure.step("Поиск всех элементов {locator}")
    def find_all(self, locator):
        """Найти все элементы (ждём появления в DOM)."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Получение текстов всех элементов {locator}")
    def get_elements_text(self, locator, strip=True):
        """Получить список текстов всех элементов."""
        elements = self.find_all(locator)
        return [el.text.strip() if strip else el.text for el in elements]
