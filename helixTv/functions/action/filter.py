from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4", "helixTv")
driver = get_driver()
wait = get_wait()

# Filter by Favorites
def filterByFavorites():
    filterButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/filters_button")'))
        )
    filterButton.click()
    time.sleep(2)
    favoritesOption = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Chaînes favorites")'))
        )
    favoritesOption.click()
    time.sleep(2)

    confirmButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/ok_button")'))
        )
    confirmButton.click()
    time.sleep(2)