import pytest
from Base.base import BaseSetup
from PO.InputPage import InputPage
from PO.Home_Page import HomePage

class TestInputPage:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = BaseSetup.initialize_driver()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_input_fields(self, setup):
        # Initialize HomePage and InputPage objects
        home_page = HomePage(self.driver)
        input_page = InputPage(self.driver)

        # Click the edit button and navigate to the edit page
        home_page.click_edit_button()

        # 1. Enter full name
        input_page.enter_full_name("Enter first & last name")

        # 2. Append text and press keyboard tab
        input_page.append_text_and_tab("I am good")

        # 3. Get the text inside the box
        text_inside_box = input_page.get_text_inside_box()
        assert text_inside_box == "ortonikc", f"Expected 'ortonikc', got {text_inside_box}"

        # 4. Clear the text
        input_page.clear_text()

        # 5. Confirm if the edit field is disabled
        is_disabled = input_page.confirm_field_disabled()
        assert is_disabled, "Field is not disabled"

        # 6. Confirm if the text is readonly
        is_readonly = input_page.confirm_text_readonly()
        assert is_readonly, "Text is readonly"
