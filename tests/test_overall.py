import allure
import pytest

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the overall function")
class TestOverall:

    @allure.story("validate the main page function")
    @allure.description("validate if register and add item to shopping cart is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_register_and_add_item_to_shopping_cart(self, initialize):
        with allure.step("start first register and add to cart test"):
            initialize.home_page.select_register()
            password = initialize.faker.password()
            expected_email = initialize.faker.email()
            initialize.register_page.fill_details(initialize.faker.first_name(), initialize.faker.last_name(),
                                                  expected_email, password)
            initialize.register_page.click_on_register()
            initialize.register_page.click_on_continue()
            actual_email = initialize.home_page.get_registered_email()
            assert expected_email == actual_email, f'user was not registered and email is not correct at the header'
            initialize.home_page.click_on_digital_downloads()
            initialize.digital_downloads_page.click_on_random_item()
            title_of_random_item = initialize.digital_downloads_page.get_title_from_item()
            initialize.digital_downloads_page.add_product_to_cart()
            initialize.digital_downloads_page.wait_for_adding_the_product_to_the_shopping_cart()
            initialize.digital_downloads_page.click_on_shopping_cart()
            actual_title_at_cart = initialize.shopping_cart_page.get_the_product_on_the_shopping_cart()
            assert actual_title_at_cart == title_of_random_item, f'product name is not the same, actual product name in cart is {actual_title_at_cart}'
