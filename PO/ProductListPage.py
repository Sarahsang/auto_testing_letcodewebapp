from selenium.webdriver.common.by import By

class ProductListPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Product List page
        self.return_to_category_link = (By.LINK_TEXT, "Return to FISH")
        self.item_links = (By.XPATH, "//div[@id='Catalog']//tr/td[1]/a")
        self.add_to_cart_buttons = (By.XPATH, "//div[@id='Catalog']//a[contains(@class, 'Button')]")

    def click_return_to_category(self):
        self.driver.find_element(*self.return_to_category_link).click()

    def click_item_by_id(self, item_id):
        """
        Click the item specified by its ID.

        Args:
            item_id (str): The ID of the item to click.

        Raises:
            NoSuchElementException: If the item is not found.
        """
        try:
            elements = self.driver.find_elements(*self.item_links)
            for element in elements:
                if element.text == item_id:
                    element.click()
                    return
        except Exception as e:
            print(f"Exception occurred while clicking item with ID {item_id}: {e}")
            raise


    def click_add_to_cart_by_item_id(self, item_id):
        elements = self.driver.find_elements(*self.item_links)
        for index, element in enumerate(elements):
            if element.text == item_id:
                self.driver.find_elements(*self.add_to_cart_buttons)[index].click()
                return

    def is_at_product_list_for(self, product_name):
        try:
            self.driver.find_element(By.XPATH, f"//h2[text()='{product_name}']")
            return True
        except:
            return False
