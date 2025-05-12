import pytest
from pages.home_page import HomePage
from utils.data_loader import load_test_data


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("testdata", load_test_data("testdata/testdata_xls.xlsx", sheet_name="Sheet1"))
    def test_verify_login_functionality_using_xlsx(self, setup, testdata):
        home_page = HomePage(setup)
        home_page.verify_login_functionality(testdata['email'], testdata['password'])

    @pytest.mark.parametrize("testdata", load_test_data("testdata/testdata_csv.csv", sheet_name="Sheet1"))
    def test_verify_login_functionality_using_csv(self, setup, testdata):
        home_page = HomePage(setup)
        home_page.verify_login_functionality(testdata['email'], testdata['password'])

    def test_verify_device_details(self,setup):
        home_page = HomePage(setup)
        home_page.validate_device_details()

    def test_verify_android_keycode(self,setup):
        home_page = HomePage(setup)
        home_page.validate_android_key_code()

