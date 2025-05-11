from appium.webdriver.appium_service import AppiumService
from utils.logger import setup_logger


class AppiumServer:
    def __init__(self):
        self.service = AppiumService()
        self.logger = setup_logger()

    def start_server(self, port=4723):
        if not self.service.is_running:
            self.service.start(args=['--port', str(port)])
            self.logger.info(f"Appium server started on port {port}")
        else:
            self.logger.error("Appium server is already running")

    def stop_server(self):
        if self.service.is_running:
            self.service.stop()
            self.logger.info("Appium server stopped")
        else:
            self.logger.error("Appium server was not running")

    def is_running(self):
        return self.service.is_running
