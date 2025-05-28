import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import random
import string

class TestCreateAd:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        yield
        self.driver.quit()

    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.ru"

    def test_create_ad_as_unauthorized_user(self, setup):
        self.driver.find_element(*Locators.POST_AD_BUTTON).click()
        assert self.driver.find_element(*Locators.MODAL_TITLE).is_displayed()

    def test_create_ad_as_authorized_user(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = self.generate_email()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))

        self.driver.find_element(*Locators.POST_AD_BUTTON).click()
        self.driver.find_element(*Locators.TITLE_INPUT).send_keys("Кольцо всевластия")
        self.driver.find_element(*Locators.CATEGORY_DROPDOWN).click()
        self.driver.find_element(*Locators.CATEGORY_OPTION).click()
        self.driver.find_element(*Locators.CONDITION_RADIO_BUTTON).click()
        self.driver.find_element(*Locators.CITY_DROPDOWN).click()
        self.driver.find_element(*Locators.CITY_OPTION).click()
        self.driver.find_element(*Locators.DESCRIPTION_INPUT).send_keys("В хорошем состоянии, пару раз надевал какой-то хоббит.")
        self.driver.find_element(*Locators.PRICE_INPUT).send_keys("1000000")
        self.driver.find_element(*Locators.PUBLISH_BUTTON).click()

        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        self.driver.find_element(*Locators.USER_AVATAR).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.MY_PROFILE))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.MY_ADS_HEADER))

        ads = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//h2[contains(@class, "h2") and text()="Кольцо всевластия"]')))
        
        assert ads.is_displayed

