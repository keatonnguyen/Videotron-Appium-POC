from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from .capabilities import Capability

def initialize_driver(app_name):
    options, server_url = Capability.get_android_options(app_name)
    
    driver = webdriver.Remote(server_url, options=options)
    wait = WebDriverWait(driver, 40)
    
    return driver, wait
