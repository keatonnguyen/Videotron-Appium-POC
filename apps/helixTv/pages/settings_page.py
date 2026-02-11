from common.base_page import BasePage

from apps.helixTv.utils.locators import ParentalCtrlLocators, SettingsLocators

from apps.helixTv.pages.parentalCtrl_page import ParentalCtrlPage

class SettingsPage(BasePage):

    def go_to_playback_preferences(self):
        self.click(SettingsLocators.PLAYBACK_PREFERENCES_SECTION)
    
    def go_to_accessibility(self):
        self.click(SettingsLocators.ACCESSIBILITY_SECTION)

    def go_to_parental_controls(self):
        self.click(SettingsLocators.PARENTAL_CONTROLS_SECTION)
        if self.is_visible(ParentalCtrlLocators.PIN_PROMPT):
            self.enter_pin()
        return ParentalCtrlPage(self.driver)

    def go_to_manage_devices(self):
        self.click(SettingsLocators.MANAGE_DEVICES_SECTION)

    def go_to_help(self):
        self.click(SettingsLocators.HELP_SECTION)
    
    def go_to_terms_of_use(self):
        self.click(SettingsLocators.TERMS_OF_USE_SECTION)
    
    def check_version(self):
        return self.get_text(SettingsLocators.APP_VERSION)
    
    