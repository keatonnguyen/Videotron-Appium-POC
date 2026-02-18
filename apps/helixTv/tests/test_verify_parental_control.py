import re
import pytest
import allure

from apps.helixTv.pages import settings_page
from apps.helixTv.utils.locators import SettingsLocators, HomeLocators, ParentalCtrlLocators


@allure.feature("Settings")
@allure.story("Verify Parental Control")
@pytest.mark.basic
@pytest.mark.helixTv

def test_verify_parental_control(helix_app):
    app = helix_app
    levels = ["Adult", "Teen", "Child"]

    # INITIAL SETUP
    assert app.home.find(HomeLocators.AIRPLAY_BUTTON).is_displayed(), "Home page"
    parental_control_page = app.home.go_to_settings().go_to_parental_control()
    parental_control_page.toggle_parental_control()
    parental_control_page.enter_pin()
    app.back().back()
    
    for i in levels:
        parental_control_page

        # Set TV ratings
        parental_control_page.get_tv_rating()
        parental_control_page.select_parental_ctrl_level(i)
        app.navigationBar.go_to_back().go_to_back().go_to_back()

        # Verify i is set
        if i == "Adult":
            liveTv_page = app.home.go_to_live_tv()
            liveTv_page.go_to_channel_340()
            assert app.is_visible(ParentalCtrlLocators.RATING_BLOCKED), f"{i} rating should be blocked"
            app.navigationBar.go_to_back().go_to_home()
        
        if i == "Teen":
            search_page = app.home.go_to_search()
            search_page.search_for("Alien: Romulus").select_first_result().play()
            assert app.is_visible(ParentalCtrlLocators.RATING_BLOCKED), f"{i} rating should be blocked"
            app.navigationBar.go_to_back().go_to_home()
        
        if i == "Child":
            search_page = app.home.go_to_search()
            search_page.search_for("Spider-Man: loin des siens").select_first_result().play()
            assert app.is_visible(ParentalCtrlLocators.RATING_BLOCKED), f"{i} rating should be blocked"
            app.navigationBar.go_to_back().go_to_home()
    
    # CLEANUP
    parental_control_page = app.home.go_to_settings().go_to_parental_control().reset_parental_ctrl().toggle_parental_ctrl()
    app.navigationBar.go_to_back().go_to_back().go_to_home()


        
        

