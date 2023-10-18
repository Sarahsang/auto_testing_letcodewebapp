from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class AlertPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the ShoppingCartPage
        self.first_select_box = (By.XPATH, "//button[@id='accept']")
        self.second_select_box = (By.XPATH, "//button[@id='confirm']")
        self.third_select_box = (By.XPATH, "//button[@id='prompt']")
        self.fourth_select_box = (By.XPATH, "//button[@id='modern']")

    def handle_simple_alert(self):
        self.driver.find_element(*self.first_alert_button).click()
        alert = Alert(self.driver)
        alert.accept()

    def handle_confirm_alert(self):
        self.driver.find_element(*self.second_alert_button).click()
        alert = Alert(self.driver)
        print(alert.text)
        alert.dismiss()

    def handle_prompt_alert(self, name):
        self.driver.find_element(*self.third_alert_button).click()
        alert = Alert(self.driver)
        alert.send_keys(name)
        alert.accept()

    def handle_modern_alert(self):
        self.driver.find_element(*self.fourth_alert_button).click()
        
    def handle_simple_alert(self):
        self.driver.find_element(*self.first_alert_button).click()
        self.driver.switch_to.alert.accept()

    def handle_confirm_alert(self):
        self.driver.find_element(*self.second_alert_button).click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()

    def handle_prompt_alert(self, name):
        self.driver.find_element(*self.third_alert_button).click()
        alert = self.driver.switch_to.alert
        alert.send_keys(name)
        alert.accept()

    def handle_modern_alert(self):
        self.driver.find_element(*self.fourth_alert_button).click()