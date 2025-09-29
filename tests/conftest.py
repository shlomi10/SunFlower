import os
os.environ["DISPLAY"] = ":99"
import allure
import pytest

from playwright.sync_api import sync_playwright

from tests.base_class import BaseClass


@pytest.fixture(scope="function", autouse=True)
def initialize(request):
    with sync_playwright() as playwright:
        headless_mode = os.getenv("HEADLESS", "true").lower() == "true"
        browser = playwright.chromium.launch(headless=headless_mode, args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        # Ensure the window is maximized using JavaScript
        page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.availWidth, screen.availHeight);")

        # Get the actual window size from the browser and adjust viewport
        window_size = page.evaluate("""() => {return { width: window.innerWidth, height: window.innerHeight };}""")
        page.set_viewport_size(window_size)

        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        base = BaseClass(page)
        page.goto(base.base_url)
        yield base

        # Capture screenshot if test fails
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:  # Checks if test failed
            screenshot_dir = "../screenshots"
            os.makedirs(screenshot_dir, exist_ok=True) # Ensure directory exists
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
