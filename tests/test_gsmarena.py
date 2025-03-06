import allure
import pytest
from playwright.sync_api import expect

from utils.constants import *

"""
This file contains the main tests
"""


@allure.epic("Functionality")
@allure.feature("title - functionality")
@allure.story("validate the gsm arena function")
class TestGsmArena:

    @pytest.fixture(autouse=True)
    def setup(self, initialize):
        """Initialize driver and page objects before each test"""
        self.home_page, self.first_article_page, self.result_page, self.pixel_page, self.page = initialize

    @allure.story("validate the main page function")
    @allure.description("validate if first article is working")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("validate basic functionality")
    @pytest.mark.flaky(reruns=1)
    def test_first_article(self):
        with allure.step("start first article test"):
            self.page.goto(BASE_URL)
            self.home_page.select_first_article()
            self.first_article_page.search_item(SEARCH_TERM)
            self.result_page.select_the_pixel_device_in_page()
            self.result_page.get_title_of_device()
            expect(self.result_page.get_title_of_device() == DEVICE_NAME), "Google Pixel 9 Pro XL was not at the page"

    @allure.story("validate title")
    @allure.description("validate title of the page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("test user land at wikipedia")
    @pytest.mark.flaky(reruns=1)
    def test_user_land_at_wiki(self):
        with allure.step("start test validate title"):
            self.page.goto(BASE_URL)
            self.home_page.select_first_article(SEARCH_TERM)
            self.home_page.click_on_recaptcha()
        with allure.step("click first result on page"):
            self.result_page.click_first_search_result_in_page()
        with allure.step("validate title of the page"):
            assert self.wiki_page.get_title_of_page() == WIKI_TITLE, "Israel - Wikipedia was not under results"
