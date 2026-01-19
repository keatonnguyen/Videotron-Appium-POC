from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import capabilities

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)


# Go to Home Section
def goToHome():
    homeSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
        )
    homeSection.click()
    time.sleep(10)

# Go to Live TV Section
def goToLiveTV():
    liveTVSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)'))
        )
    liveTVSection.click()
    time.sleep(10)

# Go to My Library Section
def goToMyLibrary():
    myLibrarySection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(12)'))
        )
    myLibrarySection.click()
    time.sleep(10)

def goToSearch():
    searchSection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(14)'))
        )
    searchSection.click()
    time.sleep(10)

def goToBack():
    backButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")'))
        )
    backButton.click()
    time.sleep(10)
