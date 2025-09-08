import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop

def test_create_order(logged_in_page):
    page = logged_in_page
    driver = page.driver  # достаем драйвер из страницы
    wait = WebDriverWait(driver, 20)

    # Конструктор
    bun = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')
        )
    )
    drop_area = driver.find_element(
        By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']"
    )
    drag_and_drop(driver, bun, drop_area)

    # Оформление заказа
    driver.find_element(By.XPATH, '//button[text()="Оформить заказ"]').click()

    # Ждем появления номера заказа
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__overlay')]")
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    wait.until(EC.invisibility_of_element_located(OVERLAY))
    time.sleep(5)  # даем время модалке обновить номер
    order_number = wait.until(lambda d: (num := d.find_element(*ORDER_NUMBER).text.strip()) != "" and num)
    print("Номер заказа:", order_number)

    # Закрытие модалки
    modal_close = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")))
    modal_close.click()

    # Переход на Ленту заказов
    feed_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//p[text()="Лента Заказов"]/parent::a')))
    time.sleep(1)
    feed_btn.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Лента заказов']")))

    # Ждем, пока заказ появится в статусе "В работе"
    def order_in_work_present(driver):
        orders = driver.find_elements(By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')
        return any(order_number in order.text for order in orders)

    wait.until(order_in_work_present)
    print(f"Заказ {order_number} появился в 'В работе'")
