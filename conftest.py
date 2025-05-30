import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()