import os

import allure
import pytest
from playwright.sync_api import sync_playwright

from pages.homePage import Homepage
from pages.resultsPage import ResultsPage
from pages.wikiPage import WikiPage


@pytest.fixture(scope="function", autouse=True)
def initialize(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        home_page = Homepage(page)
        result_page = ResultsPage(page)
        wiki_page = WikiPage(page)
        yield home_page, result_page, wiki_page, page

        screenshot_dir = "../screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)  # ✅ Ensure directory exists
        screenshot_path = f"{screenshot_dir}/{request.node.name}.png"

        # Capture screenshot if test fails
        if request.node.rep_call.failed:  # Checks if test failed
            screenshot_path = f"../screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name="screenshot", attachment_type=allure.attachment_type.PNG)

        context.tracing.stop(path="../trace/trace.zip")
        page.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to check the test result status (failed or passed).
    This is required to access test results inside fixtures.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        item.rep_call = rep  # Store test result in the request node