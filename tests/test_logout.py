import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import random
import string

class TestUser_Logout:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        yield
        self.driver.quit()

    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.ru"

    def test_successful_logout(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = self.generate_email()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert self.driver.find_element(*Locators.USER_AVATAR).is_displayed()   

        self.driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_button = self.wait.until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert login_button.is_displayed()
