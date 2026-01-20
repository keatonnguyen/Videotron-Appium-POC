from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import capabilities

# Initialize driver globally
_driver = None
_wait = None

def initialize_driver(device, app_name):
    """Initialize the Appium driver and WebDriverWait"""
    global _driver, _wait
    
    if _driver is None:
        options = capabilities.getCapabilities(device, app_name)
        _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        _wait = WebDriverWait(_driver, 15)
    
    return _driver, _wait

def get_driver():
    """Get the initialized driver"""
    return _driver

def get_wait():
    """Get the initialized WebDriverWait"""
    return _wait

def quit_driver():
    """Quit the driver"""
    global _driver, _wait
    if _driver is not None:
        _driver.quit()
        _driver = None
        _wait = None
