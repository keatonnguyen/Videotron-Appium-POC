from .base_page import BasePage
from ..utils.locators import HomeLocators

class LiveTvPage(BasePage):

    def go_to_channel_4(self):
        self.click(HomeLocators.CHANNEL_4)
    
    def go_to_channel_340(self):
        self.click(HomeLocators.CHANNEL_340)
    
    def open_filter(self):
        self.click(HomeLocators.FILTER_BUTTON)
    
    def select_favorites_filter(self):
        self.click(HomeLocators.FILTER_FAVORITES_OPTION)
        self.click(HomeLocators.FILTER_CONFIRM_BUTTON)
