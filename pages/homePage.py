import allure
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page

from pages.basePage import BasePage

"""
This file contains the main search page, where you can make search
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("First article page")
class Homepage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__first_article = page.locator(".review-column-list-item.review-column-list-item-main")

    @allure.step("click on first article")
    def select_first_article(self) -> None:
        expect(self.__first_article).to_be_visible(timeout=5000)
        self.__first_article.click()
