from playwright.sync_api import Page


class BaiduResultPage:

    def __init__(self, page):
        self.page=page
        self.search_input=page.locator("#kw")
        self.result_links=page.locator("h3.c-title>a")

    def result_link_titles(self):
        self.result_links.nth(4).wait_for()
        return self.result_links.all_text_contents()

    def result_link_titles_contain_phrase(self, phrase):
        titles=self.result_link_titles()
        match_titles=[m for m in titles if phrase.lower() in m.lower()]
        return len(match_titles)>0



