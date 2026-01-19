from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
import helixTv.functions.helix_navigator.home as home

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)


# Get RDK Version
def getVersion():
    try:
        print("Starting Session...")
        time.sleep(10)

        # Navigate to profile section
        home.goToSettings()
        time.sleep(5)

        # Get RDK Version
        rdkVersion = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and contains(@text, "Version")]'))
        )
        time.sleep(10)
        print("RDK Version: ", rdkVersion.text)
        
    finally:
        driver.quit()

getVersion()
