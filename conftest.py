import pytest
from selenium import webdriver
from data.config_urls import Urls
from web_pages.order_feed_page import OrderFeedPage
from data.data_user import UserData


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

@pytest.fixture
def logged_in_page(driver_do):
    page = OrderFeedPage(driver_do)
    page.login_user(UserData.user_email, UserData.user_password, Urls.LOGIN)
    return page
