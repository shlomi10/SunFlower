import allure
from pages.basePage import BasePage

"""
This file contains the shopping cart
"""

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Shopping cart page")
class ShoppingCartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__product_on_list = page.locator(".product-name")
        self.logger.info("ShoppingCartPage initialized with locator for product list in cart.")

    @allure.step("Get text products on the list")
    def get_the_product_on_the_shopping_cart(self) -> str:
        """Retrieve the product name text from the shopping cart."""
        self.logger.info("Fetching product name from the shopping cart.")
        product_name = self.get_text(self.__product_on_list)
        self.logger.info(f"Extracted product name from cart: {product_name}")
        return product_name
