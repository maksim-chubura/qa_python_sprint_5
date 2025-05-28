import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestUser_Login:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")
        yield
        self.driver.quit()

    def test_successful_login(self, setup):
        self.driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        self.driver.find_element(*Locators.EMAIL_INPUT).send_keys("maksim_qa@mail.ru")
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys("password123")
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

        user_avatar = self.wait.until(EC.visibility_of_element_located(Locators.USER_AVATAR))
        assert user_avatar.is_displayed()
