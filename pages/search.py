from playwright.sync_api import Page
from config.config import Config


class BaiduSearchPage:


    def __init__(self, page):
        self.page = page
        self.search_input = page.locator("#kw")
        self.search_button = page.locator("#su")

    def load(self):
        self.page.goto(Config.url)

    def search(self, phrase):
        self.search_input.fill(phrase)
        self.search_button.click()
