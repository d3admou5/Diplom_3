from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BTN = (By.XPATH, '//p[text()="Конструктор"]/parent::a')  # Кнопка "Конструктор"
    ORDERS_LIST_BTN = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # Кнопка "Лента заказов"
    BUN_CARD = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]')  # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_DETAILS_POPUP = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Детали ингредиента
    CLOSE_POPUP_BTN = (By.XPATH, '//button[contains(@class,"close")]')  # Кнопка закрытия окна ингредиента
    INGREDIENT_COUNT = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик ингредиента
    MAIN_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер"
    ORDER_BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (низ)']")  # Корзина заказа

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input") # Поле email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")  # Поле пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти"


class OrderFeedLocators:
    ORDERS_LIST_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
