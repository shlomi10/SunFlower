import logging

import allure
from playwright.sync_api import Page, Locator

from pages.basePage import BasePage

"""
This file contains the results page, where you can find results of search
"""

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Result page")
class ResultsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.google_search_result = page.locator("h3 span")
        self.first_result = self.google_search_result.first

    @allure.step("get the first result in page")
    def validate_search_result_in_page(self) -> Locator:
        print(self.google_search_result.first.inner_text())

        # logging.basicConfig(level=logging.INFO)
        # logging.info(f"First search result: {self.google_search_result.first.inner_text()}")


        return self.google_search_result.first

    @allure.step("click on first result")
    def click_first_search_result_in_page(self) -> None:
        self.click(self.first_result)
