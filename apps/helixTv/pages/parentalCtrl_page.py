from common.base_page import BasePage

from apps.helixTv.utils.locators import ParentalCtrlLocators

class ParentalCtrlPage(BasePage):

    def enter_pin(self):
        for i in range(4):
            self.click(ParentalCtrlLocators.PIN_1)

    def toggle_parental_ctrl(self):
        self.click(ParentalCtrlLocators.PARENTAL_CTRL_TOGGLE)
        if self.find(ParentalCtrlLocators.PIN_PROMPT).is_displayed():
            self.enter_pin()

    def reset_parental_ctrl(self):
        self.click(ParentalCtrlLocators.RESET_PARENTAL_CTRL_BUTTON)
    
    def get_tv_rating(self):
        self.click(ParentalCtrlLocators.TV_RATING_BUTTON)
    
    def select_parental_ctrl_level(self, level):
        if level == "Adult":
            self.click(ParentalCtrlLocators.LEVEL_ADULT)
        elif level == "Teen":
            self.click(ParentalCtrlLocators.LEVEL_TEEN)
        elif level == "Child":
            self.click(ParentalCtrlLocators.LEVEL_CHILD)
        elif level == "All":
            self.click(ParentalCtrlLocators.LEVEL_ALL)