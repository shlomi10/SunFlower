import allure

from pages.basePage import BasePage

"""
This file contains the Wiki page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Wiki page")
class WikiPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__search_field = page.get_by_placeholder("Search Wikipedia")

    @allure.step("get the page title")
    def get_title_of_page(self) -> str:
        return super().get_title_of_page()

    @allure.step("search in wikipedia")
    def search_in_wikipedia(self) -> str:
        self.fill(self.__search_field, "stam")
        self.press_enter_on_page()
        return self.get_title_of_page()
