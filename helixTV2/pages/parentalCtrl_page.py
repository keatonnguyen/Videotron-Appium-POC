from .base_page import BasePage
from ..utils.locators import ParentalCTRLLocators

class ParentalCTRLPage(BasePage):

    def enter_pin(self):
        for i in range(4):
            self.click(ParentalCTRLLocators.PIN_NUMBER_1)

    def toggle_parental_ctrl(self):
        self.click(ParentalCTRLLocators.PARENTAL_CTRL_TOGGLE)

    def reset_parental_ctrl(self):
        self.click(ParentalCTRLLocators.RESET_PARENTAL_CTRL_BUTTON)
    
    def set_tv_rating(self):
        self.click(ParentalCTRLLocators.TV_RATING_BUTTON)
    
    def select_parental_ctrl_level(self, level):
        if level == "Adult":
            self.click(ParentalCTRLLocators.LEVEL_ADULT)
        elif level == "Teen":
            self.click(ParentalCTRLLocators.LEVEL_TEEN)
        elif level == "Child":
            self.click(ParentalCTRLLocators.LEVEL_CHILD)
        elif level == "All":
            self.click(ParentalCTRLLocators.LEVEL_ALL)