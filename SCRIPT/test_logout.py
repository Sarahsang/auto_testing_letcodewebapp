from PO.Home_page import HomePage
from Data.data import USERNAME, PASSWORD


class TestLogout:

    def test_logout(self, login, setup):  # login first
        """
        Test case for logging out.

        Raises:
            AssertionError: If the test case fails.
        """
        try:
            driver = setup
            home = HomePage(driver)
            home.click_sign_out()
            assert home.is_sign_in_displayed()
        except Exception as e:
            print(f"Exception occurred during logout test: {e}")
            raise

        