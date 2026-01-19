import subprocess

from appium.options.android import UiAutomator2Options
from utils.config_reader import Config
from utils.data_loader import find_file_path


class AppiumHelper:

    @staticmethod
    def get_base_options(include_platform_version=False):
        """
        Create base Appium options common for both local and grid execution.
        """

        options = UiAutomator2Options()

        options.platform_name = Config.PLATFORM_NAME
        options.automation_name = Config.AUTOMATION_NAME
        options.device_name = Config.DEVICE_NAME
        options.udid = Config.UDID

        if include_platform_version:
            options.platform_version = Config.PLATFORM_VERSION

        options.appWaitActivity = "*"
        options.autoGrantPermissions = True

        return options

    @staticmethod
    def configure_app_installation(options, logger, app_installed):
        """
        Configure options based on whether app is already installed or not.
        """

        if app_installed:
            logger.info("App already installed – launching directly")

            options.app_package = Config.APP_PACKAGE
            options.app_activity = Config.APP_ACTIVITY

            options.noReset = True
            options.fullReset = False

        else:
            logger.info("App NOT installed – installing APK first")

            options.app = find_file_path(Config.APP_NAME)
            options.app_package = Config.APP_PACKAGE
            options.app_activity = Config.APP_ACTIVITY

            options.noReset = False
            options.fullReset = True

        return options

    @staticmethod
    def is_app_installed(package_name):
        try:
            output = subprocess.check_output(
                f"adb shell pm list packages | findstr {package_name}",
                shell=True
            ).decode()

            return package_name in output

        except Exception:
            return False
