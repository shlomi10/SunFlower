import random
from playwright.sync_api import Page, Locator
from utils.logger import get_logger


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def click(self, element: Locator):
        """Click an element (expects a Locator)."""
        self.logger.info(f"Clicking element: {element}")
        element.click()

    def click_on_random_element(self, elements: Locator):
        """Click a random element (turn Locator into a list first)."""
        all_elements = elements.all()
        if not all_elements:
            self.logger.error("No elements found to click.")
            raise ValueError("No elements found to click.")
        element = random.choice(all_elements)
        self.logger.info(f"Clicking random element: {element}")
        element.click()

    def type(self, element: Locator, text: str):
        """Type an input field (expects a Locator)."""
        self.logger.info(f"Typing text '{text}' into element: {element}")
        element.type(text)

    def fill(self, element: Locator, text: str):
        """Fill an input field (expects a Locator)."""
        self.logger.info(f"Filling element {element} with text '{text}'")
        element.fill(text)

    def press_enter_on_element(self, element: Locator):
        """press enter on element."""
        self.logger.info(f"Pressing Enter on element: {element}")
        element.press("Enter")

    def press_enter_on_page(self):
        """press enter on page."""
        self.logger.info("Pressing Enter on page.")
        self.page.keyboard.press("Enter")

    def get_title_of_page(self) -> str:
        """Get the title of the page."""
        title = self.page.title()
        self.logger.info(f"Page title: {title}")
        return title

    def get_text(self, element: Locator) -> str:
        """Get the text content of an element (expects a Locator)."""
        text = element.inner_text()
        self.logger.info(f"Extracted text: {text}")
        return text

    def is_visible(self, element: Locator) -> bool:
        """Check if an element is visible (expects a Locator)."""
        visible = element.is_visible()
        self.logger.info(f"Element visibility ({element}): {visible}")
        return visible

    def wait_for_element_to_be_visible(self, element: Locator, timeout: int = 5000):
        """Wait for an element to be visible (expects a Locator)."""
        self.logger.info(f"Waiting for element {element} to be visible (timeout={timeout})")
        element.wait_for(state="visible", timeout=timeout)

    def wait_for_loader_to_disappear(self, element: Locator, timeout: int = 10000):
        """Wait until the given element (Locator) disappears (becomes hidden)."""
        self.logger.info(f"Waiting for loader {element} to disappear (timeout={timeout})")
        element.wait_for(state="hidden", timeout=timeout)

    def take_screenshot(self, path: str = "screenshot.png"):
        """Take a screenshot of the page."""
        self.logger.info(f"Taking screenshot and saving to {path}")
        self.page.screenshot(path=path)

    def switch_to_iframe(self, locator_str: str):
        """Switch to an iframe using a selector string and return the FrameLocator object."""
        self.logger.info(f"Switching to iframe with locator: {locator_str}")
        self.page.locator(locator_str).wait_for(state="visible")
        frame = self.page.frame_locator(locator_str)
        return frame
