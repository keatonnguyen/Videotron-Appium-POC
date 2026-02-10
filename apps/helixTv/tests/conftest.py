import pytest
from ...common.driver import initialize_driver
from app import App

@pytest.fixture
def helix_app(request):
    # 1. Determine which app we are testing
    # You can get this from a marker or a CLI flag
    app_name = "helixTv" 
    
    # 2. Initialize
    driver, wait = initialize_driver(app_name)
    
    # 3. Provide the App Manager to the test
    yield App(driver)
    
    # 4. Cleanup (Always runs even if test fails)
    driver.quit()
