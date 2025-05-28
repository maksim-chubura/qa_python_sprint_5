from selenium.webdriver.common.by import By

class Locators:
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    POST_AD_BUTTON = (By.XPATH, "//button[text()='Разместить объявление']")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    MY_PROFILE = (By.XPATH, "//h1[text()='Мой профиль']")
    MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
    MY_AD = (By.XPATH, "//h2[contains(@class, 'h2')")

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, ".input_span__yWPqB")

    MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT = (By.NAME, "price")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_OPTION = (By.XPATH, "//button[.//span[text()='Хобби']]")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION = (By.XPATH, "//button[.//span[text()='Казань']]")
    CONDITION_RADIO_BUTTON = (By.XPATH, "//div[contains(@class, 'radioUnput_inputRegular__')]")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")