import pytest
from playwright.sync_api import Page, expect
from pages.search import BaiduSearchPage
from pages.result import BaiduResultPage
from common.load_baidu_search_data import load_baidu_search_data

data=load_baidu_search_data()

@pytest.mark.parametrize('phrase',data['phrases'])
def test_basic_baidu_search(page,
                            search_page,
                            result_page,
                            phrase):

    # Given the Baidu home page is displayed
    search_page.load()

    # When the user searches for a phrase
    try:
        search_page.search(phrase['phrase'])
    except Exception:
        pytest.fail("Case Failed")

    # Then the search result query is the phrase
    expect(result_page.search_input).to_have_value(phrase['phrase'])

    # And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase['phrase'])

    # And the search result title contains the phrase
    expect(page).to_have_title(phrase['expected_title'])
