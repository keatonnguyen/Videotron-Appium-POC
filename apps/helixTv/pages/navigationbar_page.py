from helixTv.pages.home_page import HomePage
from helixTv.pages.library_page import LibraryPage
from helixTv.pages.liveTv_page import LiveTvPage
from helixTv.pages.search_page import SearchPage
from ....common.base_page import BasePage

from ..utils.locators import GlobalLocators

class NavigationBar(BasePage):

    def go_to_home(self):
        self.click(GlobalLocators.HOME_SECTION)
        return HomePage(self.driver)

    def go_to_search(self):
        self.click(GlobalLocators.SEARCH_SECTION)
        return SearchPage(self.driver)
    
    def go_to_library(self):
        self.click(GlobalLocators.MY_LIBRARY_SECTION)
        return LibraryPage(self.driver)
    
    def go_to_liveTv(self):
        self.click(GlobalLocators.LIVE_TV_SECTION)
        return LiveTvPage(self.driver)
    
    def go_to_back(self):
        self.click(GlobalLocators.BACK_BUTTON)
    