import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *



class TestUserRegistration:

    def test_successful_registration(self, setup):
        self.driver = setup
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert self.driver.find_element(*Locators.USER_AVATAR).is_displayed()

    def test_registration_with_invalid_email(self, setup):
        self.driver = setup
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_invalid_email())
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text

    def test_registration_with_existing_user(self, setup):
        self.driver = setup
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        email = "maksim_qa@mail.ru"
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text