from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a') # Кнопка "Конструктор"
    ORDERS_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a') # Кнопка "Лента заказов"
    CARD_BUN = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]') # Ингредиент "Флюоресцентная булка R2-D3"
    POPUP_INGREDIENT_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]') # Детали ингредиента
    BUTTON_CLOSE_POPUP = (By.XPATH, '//button[contains(@class,"close")]') # Кнопка закрытия окна ингредиента
    INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]') # Счетчик ингредиента
