import allure
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the main search page, where you can make search
"""

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Home page")
class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__search_field = page.locator("//textarea[@name='q']")
        self.__recaptcha_iframe = "iframe[title='reCAPTCHA']"
        self.__recaptcha_checkbox = "recaptcha-anchor"

    @allure.step("search for {search_term}")
    def search_for_something(self, search_term: str) -> None:
        expect(self.__search_field).to_be_visible(timeout=5000)
        self.type(self.__search_field, search_term)
        self.press_enter_on_element(self.__search_field)

    @allure.step("click on recaptcha")
    def click_on_recaptcha(self) -> None:
        frame = self.switch_to_iframe(self.__recaptcha_iframe)  # Pass only string
        if frame:
            frame.locator(self.__recaptcha_checkbox).click()  # Click inside iframe
        else:
            print("Failed to switch to reCAPTCHA iframe")


