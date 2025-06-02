from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helpers import *
from data import *

class TestCreateAd:

    def test_create_ad_as_unauthorized_user(self, driver):
        driver.find_element(*Locators.POST_AD_BUTTON).click()
        assert driver.find_element(*Locators.MODAL_TITLE).is_displayed()

    def test_create_ad_as_authorized_user(self, driver):
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(generate_email())
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.SUBMIT_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.USER_AVATAR))

        driver.find_element(*Locators.POST_AD_BUTTON).click()
        driver.find_element(*Locators.TITLE_INPUT).send_keys("Кольцо всевластия")
        driver.find_element(*Locators.CATEGORY_DROPDOWN).click()
        driver.find_element(*Locators.CATEGORY_OPTION).click()
        driver.find_element(*Locators.CONDITION_RADIO_BUTTON).click()
        driver.find_element(*Locators.CITY_DROPDOWN).click()
        driver.find_element(*Locators.CITY_OPTION).click()
        driver.find_element(*Locators.DESCRIPTION_INPUT).send_keys("В хорошем состоянии, пару раз надевал какой-то хоббит.")
        driver.find_element(*Locators.PRICE_INPUT).send_keys("1000000")
        driver.find_element(*Locators.PUBLISH_BUTTON).click()

        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*Locators.USER_AVATAR).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.MY_PROFILE))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.MY_ADS_HEADER))

        ads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.MY_AD))
        assert "Кольцо всевластия" in ads.text

