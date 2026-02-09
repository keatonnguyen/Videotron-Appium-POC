import pytest
from utils.driver import initialize_driver, quit_driver
from pages.app import App

@pytest.fixture
def helix_app(request):
    # Pass your device and app name here
    driver, wait = initialize_driver("emulator-5554", "helixTv")
    
    # Provide the App Hub (which now uses the driver)
    yield App(driver)
    
    # Cleanup happens automatically after test is done
    quit_driver()
