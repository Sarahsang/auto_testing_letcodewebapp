import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PO.ButtonPage import ButtonPage

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

        # # Explicit wait for the edit button to be clickable
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='home']")))
        
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
