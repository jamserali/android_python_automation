import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    PLATFORM_NAME = os.getenv("PLATFORM_NAME")
    AUTOMATION_NAME = os.getenv("AUTOMATION_NAME")
    PLATFORM_VERSION = os.getenv("PLATFORM_VERSION")

    DEVICE_NAME = os.getenv("DEVICE_NAME")
    UDID = os.getenv("UDID")

    APP_PATH = os.getenv("APP_PATH")
    APP_PACKAGE = os.getenv("APP_PACKAGE")
    APP_ACTIVITY = os.getenv("APP_ACTIVITY")
    APP_NAME=os.getenv("APP_NAME")
    APP_VERSION=os.getenv("APP_VERSION")

    GRID_URL = os.getenv("GRID_URL")
    APPIUM_LOCAL_URL = os.getenv("APPIUM_LOCAL_URL")
    GRID=os.getenv("SELENIUM_GRID")
