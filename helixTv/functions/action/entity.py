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

# Play Content
def playContent():
    playButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/entity_action_text")'))
        )
    playButton.click()
    time.sleep(5)

# Add to Favorites
def addToFavorites():
    favoriteButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/entity_favorite'))
        )
    favoriteButton.click()
    time.sleep(5)

# More
def moreOptions():
    moreButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Plus d'options"))
        )
    moreButton.click()
    time.sleep(3)
