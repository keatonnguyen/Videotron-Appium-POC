from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from ...capabilities import Capability

# Initialize driver globally
_driver = None
_wait = None

def initialize_driver(device, app_name):
    global _driver, _wait
    
    if _driver is None:
        options = Capability.get_android_options(device, app_name)
        _driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        _wait = WebDriverWait(_driver, 40)
    return _driver, _wait

def quit_driver():
    global _driver, _wait
    if _driver is not None:
        _driver.quit()
        _driver = None
        _wait = None
