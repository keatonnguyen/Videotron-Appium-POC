from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.driver import initialize_driver, get_driver, get_wait, quit_driver
driver = get_driver()
wait = get_wait()

import helixTv.functions.pages.home as home



#//////////////////////////////////////////////////////////////////////////////////////////////

# Get RDK Version
def getVersion():
    try:
        # Initialize driver
        initialize_driver("Pixel 4 XL", "helixTv")
        print("Starting Session...")
        time.sleep(5)

        # Navigate to profile section
        home.goToSettings()
        time.sleep(3)

        # Get RDK Version
        rdkVersion = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and contains(@text, "Version")]'))
        )
        time.sleep(3)
        print("RDK Version: ", rdkVersion.text)
        
    finally:
        quit_driver()

getVersion()
