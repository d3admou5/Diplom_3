import pytest
from selenium import webdriver
from data.config_urls import Urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver_do(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        #options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("-private")
        #options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()
