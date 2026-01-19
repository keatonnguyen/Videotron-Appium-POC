from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from functions.actions import parentalCtrl
from functions.pages import liveTv, main

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)



# Verify Parental Control
def verifyParentalCtrl_Adult():
    levels = ["Adult", "Teen", "Child", "None"]
    test = []

    # Set parental control
    parentalCtrl.setParentalCtrl("1234")

    for level in levels:
        parentalCtrl.setParentalCtrlLevel(level, "1234")

        # Verify Adult Content Access
        liveTv.goToAdultChannel()
        pinVisibility = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helix.tv:id/adult_content_toggle")'))
        )
        if pinVisibility:
            test.append(" passed")
        else:
            test.append("failed")
        
        # Extra steps for 13+ and PG content
        if level != "Adult" :
            # Verify that 13+ content is blocked

            
            if pinVisibility:
                test.append(" passed")
            else:
                test.append(" failed")
        
        # Extra steps for PG content
        if level == "Child" :
            # Verify that child content is blocked


            if pinVisibility:
                test.append(" passed")
            else:
                test.append(" failed")

        main.goToHome()
        time.sleep(5)
        for i in test:
            print("Parental Control Level " + level + ": " + i)


    # Cleanup
    parentalCtrl.resetParentalCtrl("1234")
    parentalCtrl.disableParentalCtrl("1234")




