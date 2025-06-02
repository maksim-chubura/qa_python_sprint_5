from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *
from data import *



class TestUserRegistration:

    def test_successful_registration(self, driver):
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert driver.find_element(*Locators.USER_AVATAR).is_displayed()

    def test_registration_with_invalid_email(self, driver):
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_invalid_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text

    def test_registration_with_existing_user(self, driver):
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE))
        assert "Ошибка" in error_message.text