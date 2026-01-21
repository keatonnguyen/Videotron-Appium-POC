from modulefinder import test

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from functions.action import parentalCtrl, search, entity
from functions.navigation import navigationbar, liveTv, home, settings
from helixTv.driver import initialize_driver, get_driver, get_wait, quit_driver

# Verify Parental Control
def verifyParentalCtrl():
    print("Initializing Driver...")
    initialize_driver("Pixel 4", "helixTv")
    driver = get_driver()
    wait = get_wait()

    levels = ["Adult", "Teen", "Child"]
    test = []

    try:
        # Launch the app
        print("Launching Helix TV App...")
        driver.activate_app("com.videotron.helixtv")
        time.sleep(5)
        
        # Set parental control
        print("Setting Parental Control...")
        home.goToSettings()
        settings.goToParentalCtrl()
        parentalCtrl.setParentalCtrl()
        navigationbar.goToBack()
        navigationbar.goToBack()

        # Parental Control Level Tests
        for level in levels:
            print(f"Setting Parental Control Level to {level}...")
            navigationbar.goToHome()
            home.goToSettings()
            settings.goToParentalCtrl()
            parentalCtrl.setParentalCtrlLevel(level)
            navigationbar.goToBack()
            navigationbar.goToBack()
            navigationbar.goToBack()

            # Verify Adult Content Access
            print("Verifying Adult Content Access...")
            navigationbar.goToLiveTV()
            liveTv.goToAdultChannel()
            lock = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/playback_lock_headline")'))
            )
            if lock:
                test.append(level +" test passed (18+ content)")
            else:
                test.append(level +" test failed (18+ content)")
            navigationbar.goToBack()
            
            # 13+ Content
            if level in ["Teen", "Child"] :
                print("Verifying 13+ Content Access")
                navigationbar.goToSearch()
                search.searchContent("Alien: Romulus")
                entity.playContent()
                if lock:
                    test.append(level +" test passed (13+ content)")
                else:
                    test.append(level +" test failed (13+ content)")
                navigationbar.goToBack()
                navigationbar.goToSearch()
            
            #8+ Content
            if level in ["Child"] :
                print("Verifying 8+ Content Access")
                navigationbar.goToSearch()
                search.searchContent("Spider-Man: loin des siens")
                entity.playContent()
                if lock:
                    test.append(level +" test passed (8+ content)")
                else:
                    test.append(level +" test failed (8+ content)")
                navigationbar.goToBack()
                navigationbar.goToSearch()
            navigationbar.goToHome()
            time.sleep(5)

        print("Test Results:")
        for result in test:
            print(result + "\n")

    finally:
        # Cleanup
        print("Cleaning up...")
        home.goToSettings()
        settings.goToParentalCtrl()
        parentalCtrl.resetParentalCtrl()
        parentalCtrl.disableParentalCtrl()
        quit_driver()

verifyParentalCtrl()




