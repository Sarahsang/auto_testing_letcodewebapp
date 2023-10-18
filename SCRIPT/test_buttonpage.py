import pytest
from Base.base import BaseSetup
from PO.ButtonPage import ButtonPage
from PO.Home_Page import HomePage

class TestButtonPage:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = BaseSetup.initialize_driver()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_button_fields(self, setup):
        # Initialize HomePage and ButtonPage objects
        home_page = HomePage(self.driver)
        button_page = ButtonPage(self.driver)

        # Click the "Click" button on the home page
        home_page.click_click_button()

        # Perform various operations on the Button page
        # 1. Goto Home and come back here using driver command
        button_page.click_goto_home_and_return()

        # 2. Get the X & Y co-ordinates
        location = button_page.find_location()
        print(f"Button location: {location}")

        # 3. Find the color of the button
        color = button_page.find_color()
        print(f"Button color: {color}")

        # 4. Find the height & width of the button
        size = button_page.find_size()
        print(f"Button size: {size}")

        # 5. Confirm button is disabled
        is_disabled = button_page.is_button_disabled()
        assert is_disabled, "Button is not disabled"

        # 6. Click and Hold Button
        button_page.click_and_hold()
