from .base_page import BasePage
from ..utils.locators import SettingsLocators

class SettingsPage(BasePage):

    def go_to_playback_preferences(self):
        self.click(SettingsLocators.PLAYBACK_PREFERENCES_SECTION)
    
    def go_to_accessibility(self):
        self.click(SettingsLocators.ACCESSIBILITY_SECTION)

    def go_to_parental_controls(self):
        self.click(SettingsLocators.PARENTAL_CONTROLS_SECTION)

    def go_to_manage_devices(self):
        self.click(SettingsLocators.MANAGE_DEVICES_SECTION)

    def go_to_help(self):
        self.click(SettingsLocators.HELP_SECTION)
    
    def go_to_terms_of_use(self):
        self.click(SettingsLocators.TERMS_OF_USE_SECTION)
    
    def check_version(self):
        return self.find(SettingsLocators.APP_VERSION)
    
    