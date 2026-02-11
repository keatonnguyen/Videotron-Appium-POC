from common.base_page import BasePage

from apps.helixTv.utils.locators import HomeLocators

from apps.helixTv.pages.settings_page import SettingsPage


class HomePage(BasePage):
    def go_to_settings(self):
        self.click(HomeLocators.SETTINGS_BUTTON)
        return SettingsPage(self.driver)

    def go_to_airplay(self):
        self.click(HomeLocators.AIRPLAY_BUTTON)