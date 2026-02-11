from common.base_page import BasePage

from apps.helixTv.utils.locators import GlobalLocators

from apps.helixTv.pages.home_page import HomePage
from apps.helixTv.pages.library_page import LibraryPage
from apps.helixTv.pages.liveTv_page import LiveTvPage
from apps.helixTv.pages.search_page import SearchPage

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
    