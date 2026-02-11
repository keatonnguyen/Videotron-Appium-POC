import pytest
import json
from pathlib import Path
from common.driver import initialize_driver

from app import App


@pytest.fixture
def user_data(app_name):

    # Load user data from JSON
    data_file = Path(__file__).parent / "data" / f"{app_name}_user_data.json"
    with open(data_file, "r") as f:
        data = json.load(f)
    return data

@pytest.fixture
def helix_app(app_name):
    
    # Initialize driver
    driver, wait = initialize_driver(app_name)
    
    # Provide App manager to tests
    yield App(driver, app_name)
    
    # Cleanup
    driver.quit()
