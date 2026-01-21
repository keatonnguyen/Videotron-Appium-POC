from modulefinder import test
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from functions.action import parentalCtrl, search, entity
from functions.navigation import liveTv, main, home, settings

from helixTv.functions.driver import initialize_driver, get_driver, get_wait, quit_driver
initialize_driver("Pixel 4", "helixTv")
driver = get_driver()
wait = get_wait()


#//////////////////////////////////////////////////////////////////////////////////////////////

# Verify Parental Control
def verifyParentalCtrl():
    levels = ["Adult", "Teen", "Child"]
    test = []

    # Launch the app
    print("Launching Helix TV App")
    driver.activate_app("com.videotron.helixtv")
    time.sleep(5)
    
    # Set parental control
    print("Setting Parental Control")
    home.goToSettings()
    settings.goToParentalCtrl()
    parentalCtrl.setParentalCtrl()
    main.goToBack()
    main.goToBack()

    for level in levels:
        main.goToHome()
        home.goToSettings()
        settings.goToParentalCtrl()

        print(f"Setting Parental Control Level to {level}")
        parentalCtrl.setParentalCtrlLevel(level)
        main.goToBack()
        main.goToBack()
        main.goToBack()

        # Verify Adult Content Access
        print("Verifying Adult Content Access")
        main.goToLiveTV()
        liveTv.goToAdultChannel()
        lock = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/playback_lock_headline")'))
        )
        if lock:
            test.append(level +" test passed (18+ content)")
        else:
            test.append(level +" test failed (18+ content)")
        main.goToBack()
        
        # Extra steps for 13+ and PG content
        if level in ["Teen", "Child"] :
            print("Verifying 13+ Content Access")
            main.goToSearch()
            search.searchContent("Alien: Romulus")
            entity.playContent()
            lock = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/playback_lock_headline")'))
            )
            if lock:
                test.append(level +" test passed (13+ content)")
            else:
                test.append(level +" test passed (13+ content)")
            main.goToBack()
            main.goToSearch()
        
        if level in ["Child"] :
            print("Verifying 8+ Content Access")
            main.goToSearch()
            search.searchContent("Spider-Man: loin des siens")
            entity.playContent()
            lock = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/playback_lock_headline")'))
            )
            if lock:
                test.append(level +" test passed (8+ content)")
            else:
                test.append(level +" test failed (8+ content)")
            main.goToBack()
            main.goToSearch()

        main.goToHome()
        time.sleep(5)

    print("Test Results:")
    for result in test:
        print(result + "\n")

    # Cleanup
    print("Cleaning up...")
    home.goToSettings()
    settings.goToParentalCtrl()
    parentalCtrl.resetParentalCtrl()
    parentalCtrl.disableParentalCtrl()
    quit_driver()

verifyParentalCtrl()




