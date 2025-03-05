import allure
import pytest
from playwright.sync_api import expect

from utils.constants import *

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the search function")
class TestMainSearch:

    @pytest.fixture(autouse=True)
    def setup(self, initialize):
        """Initialize driver and page objects before each test"""
        self.home_page, self.result_page, self.wiki_page, self.page = initialize

    @allure.story("validate the search function")
    @allure.description("validate if search function is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic search function")
    @pytest.mark.flaky(reruns=1)
    def test_basic_search(self):
        with allure.step("start search function test"):
            self.page.goto(BASE_URL)
            self.home_page.search_for_something(SEARCH_TERM)
            expect(self.result_page.validate_search_result_in_page()).to_have_text(
                SEARCH_RESULT), "Israel was not under results"

    @allure.story("validate title")
    @allure.description("validate title of the page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("test user land at wikipedia")
    @pytest.mark.flaky(reruns=1)
    def test_user_land_at_wiki(self):
        with allure.step("start test validate title"):
            self.page.goto(BASE_URL)
            self.home_page.search_for_something(SEARCH_TERM)
        with allure.step("click first result on page"):
            self.result_page.click_first_search_result_in_page()
        with allure.step("validate title of the page"):
            assert self.wiki_page.get_title_of_page() == WIKI_TITLE, "Israel - Wikipedia was not under results"
