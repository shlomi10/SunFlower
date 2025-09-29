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

    @allure.step("Get text products on the list")
    def get_the_product_on_the_shopping_cart(self) -> str:
        return self.get_text(self.__product_on_list)
