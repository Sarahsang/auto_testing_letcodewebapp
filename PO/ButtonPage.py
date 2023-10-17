from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ButtonPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Fish category page
        self.first_button = (By.XPATH, "//button[@id='home']")
        self.second_button = (By.XPATH, "//button[@id='position']")
        self.third_button = (By.XPATH, "//button[@id='color']")
        self.fourth_button = (By.XPATH, "//button[@id='property']")
        self.fifth_button = (By.XPATH, "(//button[@id='isDisabled'])[1]")
        self.sixth_button = (By.XPATH, "(//button[@id='isDisabled'])[2]")
        
    def click_goto_home_and_return(self):
        self.driver.find_element(*self.first_button).click()
        self.driver.back()  

    def find_location(self):
        element = self.driver.find_element(*self.second_button)
        return element.location  # method:location

    def find_color(self):
        element = self.driver.find_element(*self.third_button)
        return element.value_of_css_property('color')  # method:value_of_css_property()

    def find_size(self):
        element = self.driver.find_element(*self.fourth_button)
        return element.size  # method:size

    def is_button_disabled(self):
        element = self.driver.find_element(*self.fifth_button)
        return not element.is_enabled()  # method:is_enabled()

    def click_and_hold(self):
        element = self.driver.find_element(*self.sixth_button)
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform() # method:click_and_hold()