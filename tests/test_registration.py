import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import random
import string


class TestUser_Registration:
    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        yield
        self.driver.quit()

    def generate_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7)) + "@mail.ru"


    def test_successful_registration(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = self.generate_email()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert self.driver.find_element(*Locators.USER_AVATAR).is_displayed()

    def test_registration_with_invalid_email(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("maksim_qa")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password12")
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys("password12")
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = self.wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text

    def test_registration_with_existing_user(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = "maksim_qa@mail.ru"
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password1234")
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys("password1234")
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = self.wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text