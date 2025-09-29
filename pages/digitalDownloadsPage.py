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

    @allure.step("Click on random item")
    def click_on_random_item(self) -> None:
        self.click_on_random_element(self.__product)

    @allure.step("Get product title")
    def get_title_from_item(self) -> str:
        return self.get_text(self.__product_title)

    @allure.step("Add product to the cart")
    def add_product_to_cart(self) -> None:
        self.click(self.__add_to_cartBTN)

    @allure.step("Select shopping cart")
    def click_on_shopping_cart(self) -> None:
        self.click(self.__shopping_cart)

    @allure.step("Wait for adding the product")
    def wait_for_adding_the_product_to_the_shopping_cart(self) -> None:
        self.wait_for_loader_to_disappear(self.__spinner)
