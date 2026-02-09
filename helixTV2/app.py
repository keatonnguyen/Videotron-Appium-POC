from pages.home_page import HomePage
from pages.parentalCtrl_page import ParentalCTRLPage
from pages.settings_page import SettingsPage
from pages.search_page import SearchPage
from pages.library_page import LibraryPage
from pages.liveTv_page import LiveTvPage

class App:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def settings(self):
        return SettingsPage(self.driver)
    
    @property
    def search(self):
        return SearchPage(self.driver)
    
    @property
    def parentalCtrl(self):
        return ParentalCtrlPage(self.driver)
    
    @property
    def liveTv(self):
        return LiveTvPage(self.driver)
    
    @property
    def library(self):
        return LibraryPage(self.driver)