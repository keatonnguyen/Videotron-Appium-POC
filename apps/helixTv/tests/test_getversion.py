import re
import pytest
import allure

from apps.helixTv.utils.locators import SettingsLocators, HomeLocators


@allure.feature("Settings")
@allure.story("Get app version")
@pytest.mark.smoke
@pytest.mark.helix

def test_getversion(helix_app):
    app = helix_app

    # Verify we are on Home page
    assert app.home.find(HomeLocators.AIRPLAY_BUTTON).is_displayed(), "Not on Home page"

    # Navigate to Settings
    settings_page = app.home.go_to_settings()

    # Read Version
    try:
        version_text = settings_page.check_version()
    except AttributeError:
        # Fallback in case
        version_text = settings_page.find(SettingsLocators.APP_VERSION).text

    allure.attach(
        version_text or "",
        name="App Version",
        attachment_type=allure.attachment_type.TEXT,
    )

