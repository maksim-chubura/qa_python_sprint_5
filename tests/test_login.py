from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *

class TestUserLogin:

    def test_successful_login(self, setup):
        self.driver = setup
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("maksim_qa@mail.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))
        assert self.driver.find_element(*Locators.USER_AVATAR).is_displayed()
