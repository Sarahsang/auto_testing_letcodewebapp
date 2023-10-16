from selenium.webdriver.common.by import By

class EditPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Product Detail page
        self.return_to_product_link = (By.LINK_TEXT, "Return to FI-SW-01")
        self.add_to_cart_button = (By.XPATH, "//a[contains(@class, 'Button')]")

    def click_return_to_product(self):
        self.driver.find_element(*self.return_to_product_link).click()

    def click_add_to_cart_by_item_id(self, item_id):
        """
        Click the "Add to Cart" button for the item specified by item_id.

        Args:
            item_id (str): The ID of the item to add to the cart.

        Raises:
            NoSuchElementException: If the elements are not found.
        """
        try:
            item_elements = self.driver.find_elements(By.XPATH, "//table//tr//td[1]")
            add_to_cart_buttons = self.driver.find_elements(By.XPATH, "//table//tr//td[5]/a")
            
            for index, item_element in enumerate(item_elements):
                if item_element.text == item_id:
                    add_to_cart_buttons[index].click()
                    return
        except Exception as e:
            print(f"Exception occurred while adding item {item_id} to cart: {e}")
            raise
