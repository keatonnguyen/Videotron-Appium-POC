from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from navigation import main

from helixTv.functions.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4", "helixTv")
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Search for a content
def searchContent(contentName):
    main.goToSearch()
    searchBox = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")'))
        )
    searchBox.click()
    time.sleep(2)
    
    searchBox = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/search_src_text")'))
        )
    searchBox.send_keys(contentName)
    time.sleep(2)

    firstResult = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/image_view")'))
        )
    firstResult.click()
    time.sleep(2)