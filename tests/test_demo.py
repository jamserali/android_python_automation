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

    def test_verify_all_locators(self,setup):
        home_page = HomePage(setup)
        home_page.validate_contact_us_form()

    def test_verify_tab_activity(self,setup):
        home_page = HomePage(setup)
        home_page.verify_tab_activity()

    def test_verify_scroll_view_and_alert(self,setup):
        home_page = HomePage(setup)
        home_page.verify_scroll_view(button="1")
        home_page.verify_scroll_view(button="2")
        home_page.verify_scroll_view(button="3")
        home_page.verify_scroll_view(button="4")
        home_page.verify_scroll_view(button="5")




