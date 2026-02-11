from common.base_page import BasePage

from apps.helixTv.utils.locators import EntityLocators

class EntityPage(BasePage):

    def play_content(self):
        self.click(EntityLocators.PLAY_BUTTON)
    
    def add_to_favorites(self):
        self.click(EntityLocators.FAVORITE_BUTTON)

    def check_more(self):
        self.click(EntityLocators.MORE_OPTIONS_BUTTON)
