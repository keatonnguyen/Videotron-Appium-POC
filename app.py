from apps.helixTv.pages.home_page import HomePage
from apps.helixTv.pages.navigationbar_page import NavigationBar
from apps.helixTv.pages.parentalCtrl_page import ParentalCtrlPage
from apps.helixTv.pages.settings_page import SettingsPage
from apps.helixTv.pages.search_page import SearchPage
from apps.helixTv.pages.library_page import LibraryPage
from apps.helixTv.pages.liveTv_page import LiveTvPage
from apps.helixTv.pages.entity_page import EntityPage

class App:
    def __init__(self, driver, app_name):
        self.driver = driver
        self.app_name = app_name
    
    # HELIX TV
    @property
    def navigationBar(self):
        if self.app_name == "helixTv":
            return NavigationBar(self.driver)
    
    @property
    def home(self):
        if self.app_name == "helixTv":
            return HomePage(self.driver)
    
    @property
    def liveTv(self):
        if self.app_name == "helixTv":
            return LiveTvPage(self.driver)
        
    @property
    def search(self):
        if self.app_name == "helixTv":
            return SearchPage(self.driver)
    
    @property
    def library(self):
        if self.app_name == "helixTv":
            return LibraryPage(self.driver)
                
    @property
    def settings(self):
        if self.app_name == "helixTv":
            return SettingsPage(self.driver)
        
    @property
    def parentalCtrl(self):
        if self.app_name == "helixTv":
            return ParentalCtrlPage(self.driver)
    
    @property
    def entity(self):
        if self.app_name == "helixTv":
            return EntityPage(self.driver)

        

    