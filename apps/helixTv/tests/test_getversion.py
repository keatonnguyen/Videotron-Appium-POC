import pytest
import allure

from app import App

@allure.feature("Application Info")
@allure.story("Retrieve application version")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.helix

def test_getversion(driver):

    # Initialize app
    helixTv = App(driver, "helixTv")

    # Quick sanity check: ensure app is on home screen
    helixTv.click(HOME_SECTION)

    # Navigate to Settings
    settings_page = helixTv.settings
    settings_page.open()

    # Retrieve app version
    app_version = settings_page.check_version()

    # Attach version to Allure report
    allure.attach(
        app_version,
        name="App Version",
        attachment_type=allure.attachment_type.TEXT
    )

    # Basic validation
    assert app_version is not None, "App version should not be None"
    assert isinstance(app_version, str), "App version should be a string"
    assert len(app_version) > 0, "App version should not be empty"
