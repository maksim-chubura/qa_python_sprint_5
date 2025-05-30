from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *

class TestUser_Logout:

    def test_successful_logout(self, setup):
        self.driver = setup
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert self.driver.find_element(*Locators.USER_AVATAR).is_displayed()   

        self.driver.find_element(*Locators.LOGOUT_BUTTON).click()

        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert login_button.is_displayed()
