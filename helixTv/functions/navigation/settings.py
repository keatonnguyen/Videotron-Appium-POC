from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from functions.action import parentalCtrl
from helixTv.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4 XL", "helixTv")
driver = get_driver()
wait = get_wait()

# Go to Done                       
def goToDone():
    doneSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")'))
        )
    doneSection.click()
    time.sleep(3)

# Go to This Device
def goToThisDevice():
    thisDeviceSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Cet appareil :")'))
        )
    thisDeviceSection.click()
    time.sleep(3)

# Go to Playback Preferences
def goToPlaybackPreferences():
    playbackPreferencesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Préférences de lecture")'))
        )
    playbackPreferencesSection.click()
    time.sleep(3)

# Go to Accessibility
def goToAccessibility():
    accessibilitySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accessibilité")'))
        )
    accessibilitySection.click()
    time.sleep(3)

# Go to Parental Controls
def goToParentalCtrl():
    parentalControlsSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contrôle parental")'))
        )
    parentalControlsSection.click()
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')))
        parentalCtrl.setPin()
    except:
        pass
    time.sleep(3)

# Go to Manage Devices
def goToManageDevices():
    manageDevicesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gérer les appareils")'))
        )
    manageDevicesSection.click()
    time.sleep(3)

# Go to Help
def goToHelp():
    helpSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aide")'))
        )
    helpSection.click()
    time.sleep(3)

# Go to Terms & Policies
def goToTermsPolicies():
    termsPoliciesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Conditions")'))
        )
    termsPoliciesSection.click()
    time.sleep(3)