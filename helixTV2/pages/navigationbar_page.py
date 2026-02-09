from .base_page import BasePage
from ..utils.locators import GlobalLocators

class HomePage(BasePage):

    def go_to_home(self):
        self.click(GlobalLocators.HOME_SECTION)

    def go_to_search(self):
        self.click(GlobalLocators.SEARCH_SECTION)
    
    def go_to_library(self):
        self.click(GlobalLocators.MY_LIBRARY_SECTION)
    
    def go_to_liveTv(self):
        self.click(GlobalLocators.LIVE_TV_SECTION)
    
    def go_to_back(self):
        self.click(GlobalLocators.BACK_BUTTON)
    