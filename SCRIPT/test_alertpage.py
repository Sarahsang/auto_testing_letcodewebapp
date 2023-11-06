import pytest
from Base.base import BaseSetup
from PO.Home_page import HomePage
from PO.AlertPage import AlertPage

class TestAlertPage:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = BaseSetup.initialize_driver()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_alerts(self, setup):
        # Initialize HomePage and AlertPage objects
        home_page = HomePage(self.driver)
        alert_page = AlertPage(self.driver)

        # Navigate to the home page and click the alert button
        home_page.click_dialog_button()  

        # 1. Accept the simple alert
        alert_page.handle_simple_alert()

        # 2. Dismiss the confirm alert and print the alert text
        alert_page.handle_confirm_alert()

        # 3. Type your name and accept the prompt alert
        alert_page.handle_prompt_alert("Your Name")

        # 4. Handle the modern alert
        alert_page.handle_modern_alert()
