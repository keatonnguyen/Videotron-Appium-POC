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

from functions.actions import parentalCtrl, search, entity
from functions.pages import liveTv, main, settings

from helixTv.functions.driver import initialize_driver, get_driver, get_wait, quit_driver
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Verify Parental Control
def verifyParentalCtrl_Adult():
    levels = ["Adult", "Teen", "Child", "All", "None"]
    test = []

    # Set parental control
    main.goToSettings()
    settings.goToParentalCtrl()
    parentalCtrl.setParentalCtrl()

    for level in levels:
        parentalCtrl.setParentalCtrlLevel(level)
        main.goToBack()
        main.goToBack()

        # Verify Adult Content Access
        liveTv.goToAdultChannel()
        lock = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/playback_lock_headline'))
        )
        if lock:
            test.append(" passed")
        else:
            test.append("failed")
        main.goToBack()
        
        # Extra steps for 13+ and PG content
        if level == "Teen" :
            main.goToSearch()
            search.searchContent("Alien: Romulus")
            entity.playContent()
            lock = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/playback_lock_headline'))
            )
            if lock:
                test.append(" passed")
            else:
                test.append(" failed")
            main.goToBack()
            time.sleep(3)
        
        if level == "Child" :
            main.goToSearch()
            search.searchContent("Spider-Man: loin des siens")
            lock = wait.until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/playback_lock_headline'))
            )
            if lock:
                test.append(" passed")
            else:
                test.append(" failed")
            main.goToBack()
            time.sleep(3)

        main.goToHome()
        time.sleep(5)
        for i in test:
            print("Parental Control Level " + level + ": " + i)


    # Cleanup
    main.goToSettings()
    settings.goToParentalCtrl()
    parentalCtrl.resetParentalCtrl()
    parentalCtrl.disableParentalCtrl()




