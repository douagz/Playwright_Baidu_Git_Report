import pytest, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.result import BaiduResultPage
from pages.search import BaiduSearchPage
from playwright.sync_api import Page


@pytest.fixture
def search_page(page):
    return BaiduSearchPage(page)


@pytest.fixture
def result_page(page):
    return BaiduResultPage(page)
