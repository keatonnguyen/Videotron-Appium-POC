from .base_page import BasePage
from ..utils.locators import HomeLocators

class HomePage(BasePage):

    def go_to_settings(self):
        self.click(HomeLocators.SETTINGS_BUTTON)

    def go_to_airplay(self):
        self.click(HomeLocators.AIRPLAY_BUTTON)