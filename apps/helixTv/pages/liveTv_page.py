from ....common.base_page import BasePage
from ..utils.locators import LiveTVLocators

class LiveTvPage(BasePage):

    def go_to_channel_4(self):
        self.click(LiveTVLocators.CHANNEL_4)
    
    def go_to_channel_340(self):
        self.click(LiveTVLocators.CHANNEL_340)
    
    def open_filter(self):
        self.click(LiveTVLocators.FILTER_BUTTON)
    
    def select_favorites_filter(self):
        self.click(LiveTVLocators.FILTER_FAVORITES_OPTION)
        self.click(LiveTVLocators.FILTER_CONFIRM_BUTTON)
