from selenium.webdriver.common.by import By

class FishCategoryPage:

    def __init__(self, driver):
        self.driver = driver

        # Define locators for elements related to the Fish category page
        self.return_to_main_menu_link = (By.LINK_TEXT, "Return to Main Menu")
        self.product_links = (By.XPATH, "//div[@id='Catalog']//td/a")
        self.product_names = (By.XPATH, "//div[@id='Catalog']//tr/td[2]")

    def click_return_to_main_menu(self):
        self.driver.find_element(*self.return_to_main_menu_link).click()

    def click_product_by_name(self, name):
        """
        Click the product specified by its name.

        Args:
            name (str): The name of the product to click.

        Raises:
            NoSuchElementException: If the product is not found.
        """
        try:
            elements = self.driver.find_elements(*self.product_names)
            for index, element in enumerate(elements):
                if element.text == name:
                    self.driver.find_elements(*self.product_links)[index].click()
                    return
        except Exception as e:
            print(f"Exception occurred while clicking product named {name}: {e}")
            raise


    def get_product_names(self):
        return [element.text for element in self.driver.find_elements(*self.product_names)]
            
    def is_at_fish_category(self):
        """
        Check if the current page is the Fish category page.

        Returns:
            bool: True if at Fish category page, False otherwise.
        """
        try:
            self.driver.find_element(By.XPATH, "//h2[text()='Fish']")
            return True
        except Exception as e:
            print(f"Exception occurred: {e}")
            return False
