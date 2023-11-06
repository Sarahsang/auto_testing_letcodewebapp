from selenium.webdriver.common.by import By
'''clicks in home page'''
class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements on the home page
        self.edit = (By.LINK_TEXT, "Edit")
        self.click = (By.LINK_TEXT, "Click")
        self.drop_down = (By.LINK_TEXT, "Drop-Down")
        self.dialog = (By.LINK_TEXT, "Dialog")
        



    def click_edit_button(self):
        self.driver.find_element(*self.edit).click()
    
    def click_click_button(self):
        self.driver.find_element(*self.click).click()
        
    def click_dropdown_button(self):
        self.driver.find_element(*self.drop_down).click()

    def click_dialog_button(self):
        self.driver.find_element(*self.dialog).click()



    def navigate_to_home_page(self):
        self.driver.get("https://letcode.in/test")
        
