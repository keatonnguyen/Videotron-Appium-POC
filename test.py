from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import capabilities

# HelixTv Capabilities
appium = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=appium)

try:
    print("Starting Session...")
    
    # Take screenshot to see current state
    driver.save_screenshot("starting_page.png")
    print("Screenshot taken")
    
    # Wait up to 10 seconds for the Get Started button to appear
    wait = WebDriverWait(driver, 10)
    get_started_button = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/get_started_button'))
    )
    print("Get Started button found!")
    get_started_button.click()
    
    # Wait for 5 seconds
    time.sleep(5)

finally:
    driver.quit()
    print("Session Closed.")