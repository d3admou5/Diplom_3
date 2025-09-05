import pytest
from selenium import webdriver
from data.config_urls import Urls

@pytest.fixture(params=['chrome', 'firefox'])
def driver_do(request):
    """Открытие браузера в режиме инкогнито"""
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")  # режим инкогнито
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("-private")  # режим инкогнито
        driver = webdriver.Firefox(options=options)
    driver.set_window_size(width=1920, height=1080)
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()

