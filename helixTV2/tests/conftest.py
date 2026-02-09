import pytest
from ..app import App
from helixTV2.utils.driver import initialize_driver, quit_driver

@pytest.fixture
def helix_app(request):
    
    # Device Name & App Name
    driver, wait = initialize_driver("Pixel 4 XL", "helixTv")
    
    yield App(driver)
    
    quit_driver()
