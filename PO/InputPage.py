from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InputPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements on the Edit page
        self.first_input_box = (By.XPATH, "//input[@id='fullName']")
        self.second_input_box = (By.XPATH, "//input[@id='join']")
        self.third_input_box = (By.XPATH, "//input[@id='getMe']")
        self.fourth_input_box = (By.XPATH, "//input[@id='clearMe']")
        self.fifth_input_box = (By.XPATH, "//input[@id='noEdit']")
        self.sixth_input_box = (By.XPATH, "//input[@id='dontwrite']")

    def enter_full_name(self, name):
        self.driver.find_element(*self.first_input_box).send_keys(name)

    def append_text_and_tab(self, text):
        elem = self.driver.find_element(*self.second_input_box)
        elem.send_keys(text)
        elem.send_keys(Keys.TAB)

    def get_text_inside_box(self):
        return self.driver.find_element(*self.third_input_box).get_attribute('value')

    def clear_text(self):
        self.driver.find_element(*self.fourth_input_box).clear()

    def confirm_field_disabled(self):
        return not self.driver.find_element(*self.fifth_input_box).is_enabled()

    def confirm_text_readonly(self):
        return self.driver.find_element(*self.sixth_input_box).get_attribute('readonly') == 'true'
