from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
import home

from helixTv.functions.driver import get_driver, get_wait
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to Done                       
def goToDone():
    home.goToSettings()
    doneSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Revenir en arrière'))
        )
    doneSection.click()
    time.sleep(10)

# Go to This Device
def goToThisDevice():
    home.goToSettings()
    thisDeviceSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Cet appareil :")'))
        )
    thisDeviceSection.click()
    time.sleep(10)

# Go to Playback Preferences
def goToPlaybackPreferences():
    home.goToSettings()
    playbackPreferencesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Préférences de lecture")'))
        )
    playbackPreferencesSection.click()
    time.sleep(10)

# Go to Accessibility
def goToAccessibility():
    home.goToSettings()
    accessibilitySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accessibilité")'))
        )
    accessibilitySection.click()
    time.sleep(10)

# Go to Parental Controls
def goToParentalCtrl():
    home.goToSettings()
    parentalControlsSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contrôle parental")'))
        )
    parentalControlsSection.click()
    time.sleep(10)

# Go to Manage Devices
def goToManageDevices():
    home.goToSettings()
    manageDevicesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gérer les appareils")'))
        )
    manageDevicesSection.click()
    time.sleep(10)

# Go to Help
def goToHelp():
    home.goToSettings()
    helpSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aide")'))
        )
    helpSection.click()
    time.sleep(10)

# Go to Terms & Policies
def goToTermsPolicies():
    home.goToSettings()
    termsPoliciesSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Conditions")'))
        )
    termsPoliciesSection.click()
    time.sleep(10)