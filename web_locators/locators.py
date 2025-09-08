from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BTN = (By.XPATH, '//p[text()="Конструктор"]/parent::a')  # Кнопка "Конструктор"
    ORDERS_LIST_BTN = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # Кнопка "Лента заказов"
    BUN_CARD = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')  # Булка "Флюоресцентная R2-D3"
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Окно с деталями ингредиента
    CLOSE_POPUP_BTN = (By.XPATH, '//button[contains(@class,"close")]')  # Кнопка закрытия окна ингредиента
    INGREDIENT_COUNT = (By.XPATH, '//p[contains(@class, "num")]')  # Счетчик ингредиента
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок страницы
    ORDER_BASKET = (By.XPATH, "//span[contains(@class,'constructor-element__text') and contains(text(),'Перетяните булочку')]")  # Корзина заказа
    ORDER_BTN = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ"
    MODAL_CLOSE_BTN = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")  # Кнопка закрытия модалки заказа
    ORDER_NUMBER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq") # Номер заказа в окне
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']") # "Лента заказов"


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # Поле пароль
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"


class OrderFeedLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок страницы "Лента заказов"
    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal__overlay')]")  # Оверлей
    COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Счетчик за сегодня
    COUNTER_TOTAL = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # Счетчик за все время
    NUMBER_IN_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li') # Номер в разделе "В работе"
