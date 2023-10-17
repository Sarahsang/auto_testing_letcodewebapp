#import sys
#sys.path.append(r'c:\Users\s1013\OneDrive\Desktop\Lincoln\693\Project\Selenium_learning')

from PO.Home_page import HomePage
from PO.FishCategoryPage import FishCategoryPage
from PO.ProductListPage import ProductListPage
from PO.ProductDetailPage import ProductDetailPage
from PO.ShoppingCartPage import ShoppingCartPage

class TestShoppingCart:
    def test_add_to_cart(self, setup, login):  # login fixture
        """
        Test case for adding an item to the shopping cart.

        Raises:
            AssertionError: If the test case fails.
        """
        try:
            driver = setup
            home_page = HomePage(driver)
            fish_category_page = FishCategoryPage(driver)
            product_list_page = ProductListPage(driver)
            product_detail_page = ProductDetailPage(driver)
            shopping_cart_page = ShoppingCartPage(driver)


            # Navigate to home page
            home_page.navigate_to_home_page()

            # Navigate to Fish Category
            home_page.click_fish_category()
            assert fish_category_page.is_at_fish_category()
            
            # Click on the product

            fish_category_page.click_product_by_name("Angelfish")
            assert product_list_page.is_at_product_list_for("Angelfish"), "Not at the Product List Page for Angelfish"


            # Add item to cart
            product_detail_page.click_add_to_cart_by_item_id("EST-1")
            assert shopping_cart_page.is_at_shopping_cart_page(), "Not at the Shopping Cart Page"


            # Verify item added to cart
            assert shopping_cart_page.is_item_added("EST-1")
        except Exception as e:
            print(f"Exception occurred during test: {e}")
            raise

    def test_modify_cart_quantity(self, setup, login):
        driver = setup
        home_page = HomePage(driver)
        fish_category_page = FishCategoryPage(driver)
        product_list_page = ProductListPage(driver)
        product_detail_page = ProductDetailPage(driver)
        shopping_cart_page = ShoppingCartPage(driver)

        # Navigate to home page
        home_page.navigate_to_home_page()

        # Navigate to Fish Category
        home_page.click_fish_category()
        assert fish_category_page.is_at_fish_category()

        # Click on the product
        fish_category_page.click_product_by_name("Angelfish")
        assert product_list_page.is_at_product_list_for("Angelfish"), "Not at the Product List Page for Angelfish"

        # Add item to cart
        product_detail_page.click_add_to_cart_by_item_id("EST-1")
        assert shopping_cart_page.is_at_shopping_cart_page(), "Not at the Shopping Cart Page"

        # Verify item added to cart
        assert shopping_cart_page.is_item_added("EST-1")

        # Update the quantity of an item in the cart
        shopping_cart_page.update_quantity_by_id("EST-1", "2")

        # Verify the cart is updated
        assert shopping_cart_page.is_quantity_updated("EST-1", "2")

    def test_remove_from_cart(self, setup, login):
        driver = setup
        home_page = HomePage(driver)
        fish_category_page = FishCategoryPage(driver)
        product_list_page = ProductListPage(driver)
        product_detail_page = ProductDetailPage(driver)
        shopping_cart_page = ShoppingCartPage(driver)

        # Navigate to home page
        home_page.navigate_to_home_page()

        # Navigate to Fish Category
        home_page.click_fish_category()
        assert fish_category_page.is_at_fish_category()

        # Click on the product
        fish_category_page.click_product_by_name("Angelfish")
        assert product_list_page.is_at_product_list_for("Angelfish"), "Not at the Product List Page for Angelfish"

        # Add item to cart
        product_detail_page.click_add_to_cart_by_item_id("EST-1")
        assert shopping_cart_page.is_at_shopping_cart_page(), "Not at the Shopping Cart Page"

        # Verify item added to cart
        assert shopping_cart_page.is_item_added("EST-1")

        # Remove item from cart
        shopping_cart_page.click_remove_item_by_id("EST-1")
        assert shopping_cart_page.is_item_removed("EST-1")
        