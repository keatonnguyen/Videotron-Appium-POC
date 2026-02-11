import re
import pytest
import allure

from apps.helixTv.utils.locators import SettingsLocators, HomeLocators

@allure.feature("Parental Control")
@allure.story("Verify Parental Control")
@pytest.mark.smoke
@pytest.mark.helixTv


def test_verify_parental_control(helix_app):
    app = helix_app

    # Sanity Check
    assert app.home.find(HomeLocators.AIRPLAY_BUTTON).is_displayed(), "Not on Home page"

    # Navigate to parental control settings
    parental_control_page = app.home.go_to_settings().go_to_parental_control()


