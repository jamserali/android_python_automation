import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.android_common_methods import CommonMethods
from utils.logger import setup_logger


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.logger = setup_logger()

    battery_locator = (AppiumBy.XPATH, '//*[@text="Battery"]')
    logon_link_loc = (AppiumBy.ID, 'com.code2lead.kwad:id/Login')
    email_field = (AppiumBy.ID, 'com.code2lead.kwad:id/Et4')
    password_field = (AppiumBy.ID, 'com.code2lead.kwad:id/Et5')
    login_btn = (AppiumBy.ID, 'com.code2lead.kwad:id/Btn3')
    enter_value_btn = (AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    enter_some_value_filed_loc = (AppiumBy.CLASS_NAME, 'android.widget.EditText')

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

    def validate_device_details(self):
        self.logger.info("Current Activity : %s", self.driver.current_activity)
        self.logger.info("Current context : %s", self.driver.current_context)
        self.logger.info("Current orientation : %s", self.driver.orientation)
        self.logger.info("Check Whether device is locked or not  : %s", self.driver.is_locked())

    def validate_android_key_code(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.enter_value_btn)).click()
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.enter_some_value_filed_loc))
        element.send_keys("Android Appium Automation")
        element.click()
        for _ in range(5):
            self.driver.press_keycode(CommonMethods.get_android_keycodes()["KEYCODE_DEL"])
