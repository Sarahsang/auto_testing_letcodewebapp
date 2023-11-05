import pytest
from PO.SelectPage import SelectPage

class TestSelectPage:

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = BaseSetup.initialize_driver()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_dropdown_lists(self, setup):
        # Initialize HomePage and SelectPage objects
        home_page = HomePage(self.driver)
        select_page = SelectPage(self.driver)

        # Navigate to home page and click the select button
        home_page.click_dropdown_button()  

        # 1. Select the apple using visible text
        select_page.select_fruit_by_visible_text("Apple")

        # 2. Select your super hero's by index (e.g., index 0 for Ant-Man)
        select_page.select_superhero_by_index(0)

        # 3. Select the last programming language and print all the options
        select_page.select_last_language_and_print_options()

        # 4. Select India using value & print the selected value
        select_page.select_country_by_value_and_print_selected("India")