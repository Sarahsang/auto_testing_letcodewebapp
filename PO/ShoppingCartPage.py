from selenium.webdriver.common.by import By

class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the ShoppingCartPage
        self.return_to_main_menu_link = (By.LINK_TEXT, "Return to Main Menu")
        self.proceed_to_checkout_button = (By.LINK_TEXT, "Proceed to Checkout")
        self.update_cart_button = (By.NAME, "updateCartQuantities")

    def click_return_to_main_menu(self):
        self.driver.find_element(*self.return_to_main_menu_link).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()

    def click_update_cart(self):
        self.driver.find_element(*self.update_cart_button).click()

    def set_quantity(self, item_id, quantity):
        quantity_input = (By.NAME, item_id)
        self.driver.find_element(*quantity_input).clear()
        self.driver.find_element(*quantity_input).send_keys(quantity)

    def is_cart_empty(self):
        try:
            self.driver.find_element(By.XPATH, "//td[contains(text(), 'Your cart is empty.')]")
            return True
        except:
            return False

    def is_item_added(self, item_id):
        item_elements = self.driver.find_elements(By.XPATH, "//table//tr//td[1]")
        for item_element in item_elements:
            if item_element.text == item_id:
                return True
        return False

    def is_at_shopping_cart_page(self):
        try:
            self.driver.find_element(By.XPATH, "//h2[text()='Shopping Cart']")
            return True
        except:
            return False

    def click_remove_item_by_id(self, item_id):
        remove_button = self.driver.find_element(By.XPATH, f"//td/a[contains(@href, 'workingItemId={item_id}')]") #a tag with href containing workingItemId
        remove_button.click()
        
            
    def is_item_removed(self, item_id):
        try:
            # Try to find the item
            self.driver.find_element(By.XPATH, f"//td[text()='{item_id}']")
            return False  # If found, the item is not removed
        except:
            return True  # If not found, the item is removed
        
    def update_quantity_by_id(self, item_id, quantity):
        quantity_field = self.driver.find_element(By.NAME, item_id)
        quantity_field.clear()
        quantity_field.send_keys(quantity)
        self.click_update_cart()
        
    def is_quantity_updated(self, item_id, quantity):
        quantity_field = self.driver.find_element(By.NAME, item_id)
        return quantity_field.get_attribute("value") == quantity