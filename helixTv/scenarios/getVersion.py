from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.navigation import home, navigationbar
from helixTv.driver import initialize_driver, get_driver, get_wait, quit_driver

# Get RDK Version
def getVersion():
    try:
        print("Initializing Driver...")
        initialize_driver("Pixel 4", "helixTv")
        driver = get_driver()
        wait = get_wait()

        print("Starting Session...")
        driver.activate_app("com.videotron.helixtv")
        time.sleep(5)

        # Navigate to profile section
        navigationbar.goToHome()
        home.goToSettings()
        time.sleep(2)

        # Get RDK Version
        navigationbar.scrollDown()
        rdkVersion = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and contains(@text, "Version")]'))
        )
        print("RDK Version: ", rdkVersion.text)
        navigationbar.goToBack()
        
    finally:
        quit_driver()

getVersion()
