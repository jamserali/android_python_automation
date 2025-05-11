import os
from datetime import datetime
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.logger import setup_logger


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # This hook lets you inspect the result of a test call
    outcome = yield
    rep = outcome.get_result()

    # Only act on actual test call failures, not setup/teardown
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")  # Access the Appium driver passed as a fixture
        if driver:
            # Create screenshots directory if not exists
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Format filename with test name and timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            destination_file = os.path.join(screenshots_dir, file_name)

            # Save screenshot
            driver.save_screenshot(destination_file)
            print(f"\nScreenshot saved to {destination_file}")


@pytest.fixture(scope="session")
def logger():
    return setup_logger()


def pytest_addoption(parser):
    parser.addoption("--platform-version", action="store", default="16", help="Android platform version")
    parser.addoption("--device-name", action="store", default="emulator-5554", help="Device name")
    parser.addoption("--app-path", action="store", default="D://Android_Automation/apk/Android_Demo_App.apk",
                     help="Path to the app file")
    parser.addoption("--app_package", action="store", default="com.code2lead.kwad")
    parser.addoption("--app_activity", action="store", default="com.code2lead.kwad.MainActivity")


@pytest.fixture
def setup(request, logger):
    platform_version = request.config.getoption("--platform-version")
    device_name = request.config.getoption("--device-name")
    app_path = request.config.getoption("--app-path")
    app_package = request.config.getoption("--app_package")
    app_activity = request.config.getoption("--app_activity")

    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'platformVersion': platform_version,
        'deviceName': device_name,
        'app': app_path,
        'appPackage': app_package,
        'appActivity': app_activity
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    request.cls.driver = driver if hasattr(request, 'cls') else driver

    logger.info(f"\n##### Starting test: {request.node.name} #####")

    yield driver
    logger.info(f"#####  Finished test: {request.node.name} ##### \n")
    driver.quit()
