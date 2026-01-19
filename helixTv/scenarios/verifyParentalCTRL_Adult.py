from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
import helixTv.functions.helix_functions.parentalCtrl as parentalCtrl
import helixTv.functions.helix_navigator.liveTv as liveTv

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)


# Verify Parental Control
def verifyParentalCtrl_Adult():

    # Set parental control to adult
    parentalCtrl.setParentalCtrl("1234")

    # Verify Adult Content Access
    liveTv.goToAdultChannel()
    
    adultContentToggle = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helix.tv:id/adult_content_toggle")'))
    )
    isEnabled = adultContentToggle.get_attribute("checked")
    
    if isEnabled == "true":
        print("Adult content access is enabled.")
    else:
        print("Adult content access is disabled.")

    # Cleanup
    parentalCtrl.disableParentalCtrl()
    parentalCtrl.resetParentalCtrl()




