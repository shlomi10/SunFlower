import allure
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the main page
"""

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("First article page")
class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__register = page.locator(".ico-register")
        self.__emailHeader = page.locator(".header-links a.account")
        self.__digital_downloads = page.locator(".top-menu a[href='/digital-downloads']")
        self.logger.info("Homepage initialized with locators for Register, Email Header, and Digital Downloads.")

    @allure.step("click on register")
    def select_register(self) -> None:
        """Click on the 'Register' button."""
        self.logger.info("Waiting for 'Register' button to be visible.")
        expect(self.__register).to_be_visible(timeout=5000)
        self.logger.info("Register button is visible. Clicking on it now.")
        self.click(self.__register)
        self.logger.info("Clicked on 'Register' successfully.")

    @allure.step("get registered email")
    def get_registered_email(self) -> str:
        """Retrieve the registered user's email from the header."""
        self.logger.info("Waiting for registered email element to be visible in header.")
        expect(self.__emailHeader).to_be_visible(timeout=5000)
        email = self.get_text(self.__emailHeader)
        self.logger.info(f"Extracted registered email from header: {email}")
        return email

    @allure.step("click on digital downloads")
    def click_on_digital_downloads(self) -> None:
        """Click on the 'Digital Downloads' link in the top menu."""
        self.logger.info("Waiting for 'Digital Downloads' link to be visible.")
        expect(self.__digital_downloads).to_be_visible(timeout=5000)
        self.logger.info("'Digital Downloads' link is visible. Clicking on it.")
        self.click(self.__digital_downloads)
        self.logger.info("Clicked on 'Digital Downloads' link successfully.")
