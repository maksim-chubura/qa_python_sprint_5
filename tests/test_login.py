from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *
from data import *

class TestUserLogin:

    def test_successful_login(self, driver):
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert driver.find_element(*Locators.USER_AVATAR).is_displayed()
