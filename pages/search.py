import allure
from playwright.sync_api import Page
from common.log import Logger
from config.config import Config


class BaiduSearchPage:

    logger=Logger('BaiduSearchPage').getlog()

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_input = page.locator("#kw")
        self.search_button = page.locator("#su")

    def load(self) -> None:
        self.page.goto(Config.url)
        self.logger.info(f'Aceess {Config.url}')

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()
        self.logger.info(f'Search {phrase}')
