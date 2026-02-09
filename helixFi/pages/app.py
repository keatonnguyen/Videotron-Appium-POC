from pages.home_page import HomePage
from helixFi.pages.profile_page import ProfilePage
from helixFi.pages.wifi_page import WifiPage
from helixFi.pages.overview_page import OverviewPage

class App:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def overview(self):
        return OverviewPage(self.driver)
    
    @property
    def profile(self):
        return ProfilePage(self.driver)
    
    @property
    def wifi(self):
        return WifiPage(self.driver)