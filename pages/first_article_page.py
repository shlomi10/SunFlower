import allure

from pages.basePage import BasePage

"""
This file contains the first article page
"""


@allure.severity(allure.severity_level.CRITICAL)
@allure.story("First article page")
class FirstArticlePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__search_field = page.locator("//input[@name='sSearch']")

    @allure.step("search for {search_term}")
    def search_item(self, search_term: str) -> None:
        self.type(self.__search_field, search_term)
        self.press_enter_on_element(self.__search_field)
