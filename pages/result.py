import allure
from playwright.sync_api import Page
from common.log import Logger

class BaiduResultPage:

    logger=Logger('BaiduResultPage').getlog()

    def __init__(self, page: Page) -> None:
        self.page=page
        self.search_input=page.locator("#kw")
        self.result_links=page.locator("h3.c-title>a")

    def result_link_titles(self) -> list[str]:
        self.result_links.nth(4).wait_for()
        self.logger.info("Get search result links")
        return self.result_links.all_text_contents()

    def result_link_titles_contain_phrase(self, phrase: str) -> bool:
        titles=self.result_link_titles()
        match_titles=[m for m in titles if phrase.lower() in m.lower()]
        self.logger.info(f"Get {len(match_titles)} matched titles")
        return len(match_titles)>0



