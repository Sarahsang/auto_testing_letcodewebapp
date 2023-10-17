from selenium.webdriver.common.by import By

class AlertPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the ShoppingCartPage
        self.first_select_box = (By.XPATH, "//button[@id='accept']")
        self.second_select_box = (By.XPATH, "//button[@id='confirm']")
        self.third_select_box = (By.XPATH, "//button[@id='prompt']")
        self.fourth_select_box = (By.XPATH, "//button[@id='modern']")

    