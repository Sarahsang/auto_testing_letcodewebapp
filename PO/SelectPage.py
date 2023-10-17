from selenium.webdriver.support.ui import Select

class SelectPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Product List page
        self.first_select_box = (By.XPATH, "//select[@id='fruits']")
        self.second_select_box = (By.XPATH, "//select[@id='superheros']")
        self.third_select_box = (By.XPATH, "//select[@id='lang']")
        self.fourth_select_box = (By.XPATH, "//select[@id='country']")

    
    def select_fruit_by_visible_text(self, fruit):
        select = Select(self.driver.find_element(*self.first_select_box))
        select.select_by_visible_text(fruit)

    def select_superhero_by_index(self, index):
        select = Select(self.driver.find_element(*self.second_select_box))
        select.select_by_index(index)

    def select_last_language_and_print_options(self):
        select = Select(self.driver.find_element(*self.third_select_box))
        options = [option.text for option in select.options]
        print("All options:", options)
        select.select_by_index(len(options) - 1)

    def select_country_by_value_and_print_selected(self, value):
        select = Select(self.driver.find_element(*self.fourth_select_box))
        select.select_by_value(value)
        print("Selected value:", select.first_selected_option.text)
        
    def is_multiple(self, select_box):
        select = Select(self.driver.find_element(*select_box))
        return select.is_multiple
    
    def select_multiple_values(self, select_box, *values):
        select = Select(self.driver.find_element(*select_box))
        for value in values:
            select.select_by_visible_text(value)