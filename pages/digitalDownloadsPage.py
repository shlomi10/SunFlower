import allure
from pages.basePage import BasePage

"""
This file contains the digital downloads page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Select random item")
@allure.description("Select random item")
class DigitalDownloadsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__product = page.locator(".product-title")
        self.__add_to_cartBTN = page.locator(".add-to-cart-button")
        self.__product_title = page.locator("//h1[@itemprop='name']")
        self.__shopping_cart = page.locator(".header-links .ico-cart")
        self.__spinner = page.locator(".loading-image")
        self.logger.info("DigitalDownloadsPage initialized with all locators.")

    @allure.step("Click on random item")
    def click_on_random_item(self) -> None:
        """Click on a random product from the list."""
        self.logger.info("Attempting to click on a random product from the digital downloads list.")
        self.click_on_random_element(self.__product)
        self.logger.info("Clicked on a random product successfully.")

    @allure.step("Get product title")
    def get_title_from_item(self) -> str:
        """Get the product title text."""
        self.logger.info("Fetching product title from product page.")
        title = self.get_text(self.__product_title)
        self.logger.info(f"Extracted product title: {title}")
        return title

    @allure.step("Add product to the cart")
    def add_product_to_cart(self) -> None:
        """Add the selected product to the shopping cart."""
        self.logger.info("Clicking on 'Add to Cart' button.")
        self.click(self.__add_to_cartBTN)
        self.logger.info("'Add to Cart' button clicked successfully.")

    @allure.step("Select shopping cart")
    def click_on_shopping_cart(self) -> None:
        """Click on the shopping cart icon to navigate to the cart."""
        self.logger.info("Clicking on shopping cart icon.")
        self.click(self.__shopping_cart)
        self.logger.info("Navigated to the shopping cart page.")

    @allure.step("Wait for adding the product")
    def wait_for_adding_the_product_to_the_shopping_cart(self) -> None:
        """Wait for the spinner/loader to disappear after adding a product."""
        self.logger.info("Waiting for loader to disappear after adding product to cart.")
        self.wait_for_loader_to_disappear(self.__spinner)
        self.logger.info("Loader disappeared — product successfully added to cart.")
