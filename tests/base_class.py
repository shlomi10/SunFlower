import logging
import os

import faker
from dotenv import load_dotenv

from pages.digitalDownloadsPage import DigitalDownloadsPage
from pages.homePage import Homepage
from pages.registerPage import RegisterPage
from pages.shoppingCartPage import ShoppingCartPage

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

"""
This file contains the base class
"""


class BaseClass:
    def __init__(self, page):
        self.page = page
        self.faker = faker.Faker()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.base_url = os.getenv("BASE_URL")
        self.register_page = RegisterPage(self.page)
        self.home_page = Homepage(self.page)
        self.digital_downloads_page = DigitalDownloadsPage(self.page)
        self.shopping_cart_page = ShoppingCartPage(self.page)
        self.logger.info("Initialized BaseClass with all page objects.")
