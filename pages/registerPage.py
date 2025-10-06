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
        self.logger.info("RegisterPage initialized with all registration form locators.")

    @allure.step("fill details")
    def fill_details(self, firstName: str, lastName: str, email: str, password: str) -> None:
        """Fill in user registration details."""
        self.logger.info("Waiting for 'Register' button to become visible before filling the form.")
        expect(self.__registerBTN).to_be_visible(timeout=5000)

        self.logger.info(f"Typing first name: {firstName}")
        self.type(self.__firstName_field, firstName)

        self.logger.info(f"Typing last name: {lastName}")
        self.type(self.__lastName_field, lastName)

        self.logger.info(f"Typing email: {email}")
        self.type(self.__emailField, email)

        self.logger.info("Typing password and confirming it.")
        self.type(self.__password, password)
        self.type(self.__confirm_password, password)

        self.logger.info("Finished filling in registration details successfully.")

    @allure.step("click on register")
    def click_on_register(self):
        """Click on the register button to submit the form."""
        self.logger.info("Waiting for 'Register' button to be visible before clicking.")
        expect(self.__registerBTN).to_be_visible(timeout=5000)
        self.logger.info("Clicking on 'Register' button.")
        self.click(self.__registerBTN)
        self.logger.info("'Register' button clicked successfully.")

    @allure.step("click on continue")
    def click_on_continue(self):
        """Click on the continue button after successful registration."""
        self.logger.info("Waiting for 'Continue' button to appear after registration.")
        expect(self.__continueBTN).to_be_visible(timeout=5000)
        self.logger.info("Clicking on 'Continue' button to proceed.")
        self.click(self.__continueBTN)
        self.logger.info("'Continue' button clicked successfully, moving forward.")
