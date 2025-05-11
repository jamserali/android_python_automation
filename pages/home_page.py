from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from utils.appium_actions import AppiumActions
from utils.logger import setup_logger


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        # self.actions = AppiumActions(driver)
        self.logger = setup_logger()

    battery_locator = (AppiumBy.XPATH, '//*[@text="Battery"]')
    logon_link_loc = (AppiumBy.ID, 'com.code2lead.kwad:id/Login')
    email_field = (AppiumBy.ID, 'com.code2lead.kwad:id/Et4')
    password_field = (AppiumBy.ID, 'com.code2lead.kwad:id/Et5')
    login_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn3')

    def verify_login_functionality(self, email, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.logon_link_loc)).click()
        self.logger.info("Click on login link")

        self.wait.until(expected_conditions.visibility_of_element_located(self.email_field)).send_keys(email)
        self.logger.info("Enter email field....")

        self.wait.until(expected_conditions.visibility_of_element_located(self.password_field)).send_keys(password)
        self.logger.info("Enter password field....")

        self.wait.until(expected_conditions.visibility_of_element_located(self.login_btn)).click()
        self.logger.info("Click on login button")

    def verify_battery(self):
        battery_element = self.wait.until(
            expected_conditions.element_to_be_clickable(self.battery_locator))
        battery_element.click()
        return self
