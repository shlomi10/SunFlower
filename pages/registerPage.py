import allure
from playwright.sync_api import expect

from pages.basePage import BasePage

"""
This file contains the register page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("First article page")
class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__registerBTN = page.locator("#register-button")
        self.__firstName_field = page.locator("#FirstName")
        self.__lastName_field = page.locator("#LastName")
        self.__emailField = page.locator("#Email")
        self.__password = page.locator("#Password")
        self.__confirm_password = page.locator("#ConfirmPassword")
        self.__continueBTN = page.locator(".register-continue-button")

    @allure.step("fill details")
    def fill_details(self, firstName: str, lastName: str, email:str, password:str) -> None:
        expect(self.__registerBTN).to_be_visible(timeout=5000)
        self.type(self.__firstName_field, firstName)
        self.type(self.__lastName_field, lastName)
        self.type(self.__emailField, email)
        self.type(self.__password, password)
        self.type(self.__confirm_password, password)

    def click_on_register(self):
        expect(self.__registerBTN).to_be_visible(timeout=5000)
        self.click(self.__registerBTN)

    def click_on_continue(self):
        expect(self.__continueBTN).to_be_visible(timeout=5000)
        self.click(self.__continueBTN)
