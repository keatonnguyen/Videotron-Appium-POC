import pytest
from common.driver import initialize_driver
from app import App

@pytest.fixture
def helix_app(request):

    # 1. App name
    app_name = "helixTv" 
    
    # 2. Initialize
    driver, wait = initialize_driver(app_name)
    
    # 3. Provide the App Manager to the test
    yield App(driver, app_name)
    
    # 4. Cleanup (Always runs even if test fails)
    driver.quit()
