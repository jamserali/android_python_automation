import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from testdata.data import Data
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
    # Types of locator
    # By Index value
    contact_us_form_link = (AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")
    # By className
    enter_name_field = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    # using resourceId
    enter_email_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.code2lead.kwad:id/Et3")')
    # Using Text
    enter_mobile_number_field = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Mobile No")')
    # Using Text
    submit_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SUBMIT")')
    # using ID
    address_field = (AppiumBy.ID, 'com.code2lead.kwad:id/Et6')
    # Tab Activity
    tab_activity_btn = (AppiumBy.ID, "com.code2lead.kwad:id/TabView")
    home_tab = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("HOME")')
    home_fragment_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("HomeFragment")')
    sports_tab = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SPORT")')
    sports_fragment_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SportFragment")')
    movie_tab = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MOVIE")')
    movie_fragment_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("MovieFragment")')

    # Scroll view
    scroll_view_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ScrollView")')
    scroll_view_button1_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON1")')
    scroll_view_button2_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON2")')
    scroll_view_button3_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON3")')
    scroll_view_button4_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON4")')
    scroll_view_button5_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON5")')
    scroll_view_button6_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON6")')
    scroll_view_button7_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON7")')
    scroll_view_button8_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON8")')
    scroll_view_button9_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON9")')
    scroll_view_button10_loc = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BUTTON10")')
    yes_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("YES")')
    no_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NO")')



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

    def validate_contact_us_form(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.contact_us_form_link)).click()
        name_field = self.wait.until(expected_conditions.visibility_of_element_located(self.enter_name_field))
        name_field.send_keys(Data.NAME)
        email_field = self.wait.until(expected_conditions.visibility_of_element_located(self.enter_email_field))
        email_field.send_keys(Data.EMAIL)
        address_field = self.wait.until(expected_conditions.visibility_of_element_located(self.address_field))
        address_field.send_keys(Data.ADDRESS)
        mobile_number_field = self.wait.until(
            expected_conditions.visibility_of_element_located(self.enter_mobile_number_field))
        mobile_number_field.send_keys(Data.MOBILE)
        self.wait.until(expected_conditions.visibility_of_element_located(self.submit_btn)).click()

    def verify_tab_activity(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.tab_activity_btn)).click()
        self.wait.until(expected_conditions.visibility_of_element_located(self.home_tab)).click()
        home_fragment = self.wait.until(expected_conditions.visibility_of_element_located(self.home_fragment_loc)).text
        assert home_fragment == "HomeFragment","Home fragment text is not matching"
        self.wait.until(expected_conditions.visibility_of_element_located(self.sports_tab)).click()
        sports_fragment = self.wait.until(expected_conditions.visibility_of_element_located(self.sports_fragment_loc)).text
        assert sports_fragment == "SportFragment", "Sport fragment text is not matching"
        self.wait.until(expected_conditions.visibility_of_element_located(self.movie_tab)).click()
        movie_fragment = self.wait.until(expected_conditions.visibility_of_element_located(self.movie_fragment_loc)).text
        assert movie_fragment == "MovieFragment", "Movie fragment text is not matching"

    def verify_scroll_view(self, button):
        self.wait.until(expected_conditions.visibility_of_element_located(self.scroll_view_button)).click()

        button_locators = {
            "1": self.scroll_view_button1_loc,
            "2": self.scroll_view_button2_loc,
            "3": self.scroll_view_button3_loc,
            "4": self.scroll_view_button4_loc,
            "5": self.scroll_view_button5_loc
        }

        if button in button_locators:
            self.wait.until(expected_conditions.visibility_of_element_located(button_locators[button])).click()
        else:
            raise ValueError(f"Invalid button number: {button}")

        self.wait.until(expected_conditions.visibility_of_element_located(self.yes_btn)).click()



