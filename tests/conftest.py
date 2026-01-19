import base64
import os
from datetime import datetime
import pytest
import pytest_html
from appium import webdriver
from appium.options.android import UiAutomator2Options
from testdata.data import Data
from utils.appium_helper import AppiumHelper
from utils.config_reader import Config
from utils.data_loader import get_file_path, find_file_path
from utils.logger import setup_logger
import allure
import subprocess


# html & Allure report hook
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call":
        rep.extras = getattr(rep, "extras", [])
        if rep.failed:
            # Create timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            rep.extras.append(pytest_html.extras.html("❌ FAILED"))
            screenshot_dir = "screenshots"
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)
            os.makedirs(screenshot_dir, exist_ok=True)
            driver = item.session._driver
            driver.save_screenshot(file_path)

            with open(file_path, "rb") as f:
                image_bytes = f.read()
                encoded = base64.b64encode(image_bytes).decode("utf-8")

            rep.extras.append(
                pytest_html.extras.image(
                    encoded,
                    mime_type="image/png",
                    extension="png"
                )
            )
            allure.attach(
                image_bytes,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        elif rep.passed:
            rep.extras.append(pytest_html.extras.html("✅ PASSED"))


@pytest.fixture(scope="function")
def logger():
    return setup_logger()


def pytest_addoption(parser):
    parser.addoption("--platform-version", action="store", default=Data.PLATFORM_VERSION, help="Android platform version")
    parser.addoption("--device-name", action="store", default=Data.DEVICE_NAME, help="Device name")
    parser.addoption("--app-path", action="store", default=find_file_path(Data.APK_NAME),
                     help="Path to the app file")
    parser.addoption("--app_package", action="store", default=Data.PACKAGE_NAME)
    parser.addoption("--app_activity", action="store", default=Data.APP_ACTIVITY)
    parser.addoption("--grid-url", action="store", default=None,
                     help="Selenium Grid URL e.g. http://localhost:4444")


@pytest.fixture(scope="function")
def setup(request, logger):

    grid_url = request.config.getoption("--grid-url")
    app_installed = AppiumHelper.is_app_installed(Config.APP_PACKAGE)

    if grid_url and grid_url.strip():
        executor = grid_url
        logger.info(f"Running tests on Selenium GRID: {executor}")

        options = AppiumHelper.get_base_options(include_platform_version=False)
        options.newCommandTimeout = 300

    else:
        executor = Config.APPIUM_LOCAL_URL
        logger.info("Running tests on LOCAL Appium server")

        options = AppiumHelper.get_base_options(include_platform_version=True)
        options.newCommandTimeout = 100


    options = AppiumHelper.configure_app_installation(options, logger, app_installed)

    driver = webdriver.Remote(
        command_executor=executor,
        options=options
    )

    request.session._driver = driver
    request.cls.driver = driver if hasattr(request, 'cls') else driver

    logger.info(f"Starting test: {request.node.name}")

    yield driver

    logger.info(f"Finished test: {request.node.name}")
    driver.quit()
