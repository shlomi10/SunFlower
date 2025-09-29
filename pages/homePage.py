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

    @allure.step("click on register")
    def select_register(self) -> None:
        expect(self.__register).to_be_visible(timeout=5000)
        self.click(self.__register)

    @allure.step("get registered email")
    def get_registered_email(self) -> str:
        expect(self.__emailHeader).to_be_visible(timeout=5000)
        return self.get_text(self.__emailHeader)

    @allure.step("get registered email")
    def click_on_digital_downloads(self) -> None :
        expect(self.__digital_downloads).to_be_visible(timeout=5000)
        self.click(self.__digital_downloads)