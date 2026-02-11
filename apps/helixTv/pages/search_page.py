from common.base_page import BasePage

from apps.helixTv.utils.locators import SearchLocators

from apps.helixTv.pages.entity_page import EntityPage

class SearchPage(BasePage):

    def search_content(self, content_name):
        self.click(SearchLocators.SEARCH_BOX)
        self.type(SearchLocators.SEARCH_TEXT, content_name)
        self.click(SearchLocators.FIRST_RESULT)
        return EntityPage(self.driver)
