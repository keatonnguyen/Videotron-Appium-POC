from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path

# Add paths for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4 XL", "helixTv")
driver = get_driver()
wait = get_wait()


#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to Home Section
def goToHome():
    homeSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accueil")'))
        )
    homeSection.click()
    time.sleep(3)

# Go to Live TV Section
def goToLiveTV():
    liveTVSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Télé en direct")'))
        )
    liveTVSection.click()
    time.sleep(3)

# Go to My Library Section
def goToMyLibrary():
    myLibrarySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ma bibliothèque")'))
        )
    myLibrarySection.click()
    time.sleep(3)

def goToSearch():
    searchSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Parcourir")'))
        )
    searchSection.click()
    time.sleep(3)

def goToBack():
    backButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")'))
        )
    backButton.click()
    time.sleep(3)

def scrollDown():
    driver.swipe(500, 1500, 500, 300, 500)
    time.sleep(3)
