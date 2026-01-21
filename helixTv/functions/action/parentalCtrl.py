from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.navigation import navigationbar
from helixTv.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4", "helixTv")
driver = get_driver()
wait = get_wait()

# Set PIN
def setPin():
    pinCode =["keypadOne", "keypadTwo", "keypadThree", "keypadFour"]
    for digit in pinCode:
            pinButton = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.videotron.helixtv:id/{digit}")'))
                )
            pinButton.click()
            time.sleep(2)
    time.sleep(3)

# Set Parental Control
def setParentalCtrl():
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/switch_widget")'))
        )
    enableParentalCtrlButton.click()
    time.sleep(2)
    setPin()
    time.sleep(2)
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')))
        setPin()
        time.sleep(2)
    except:
        pass

# Disable Parental Control
def disableParentalCtrl():
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/switch_widget")'))
        )
    enableParentalCtrlButton.click()
    time.sleep(2)
    setPin()
    time.sleep(2)
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')))
        setPin()
        time.sleep(2)
    except:
        pass

# Reset Parental Control
def resetParentalCtrl():
    navigationbar.scrollDown()
    time.sleep(2)
    resetButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Réinitialiser les restrictions")'))
        )
    resetButton.click()
    time.sleep(2)

# Set Parental Control Level
def setParentalCtrlLevel(level):
    tvRatingButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Classement d’émission de télévision (français)")'))
        )  
    tvRatingButton.click()
    time.sleep(2)

    if level == "Adult":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("18+")'))
            )
        levelButton.click()
        time.sleep(2)

    elif level == "Teen":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(2)

    elif level == "Child":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8+, 13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(2)

    elif level == "All":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("G, 8+, 13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(2)