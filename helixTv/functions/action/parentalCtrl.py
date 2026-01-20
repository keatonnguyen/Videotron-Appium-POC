from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from navigation import main

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)

from helixTv.functions.driver import get_driver, get_wait
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Set PIN
def setPin():
    pinCode =["keypadOne", "keypadTwo", "keypadThree", "keypadFour"]

    for digit in pinCode:
            pinButton = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{digit}")'))
                )
            pinButton.click()
            time.sleep(3)
    time.sleep(3)

# Set Parental Control
def setParentalCtrl():
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'android:id/switch_widget'))
        )
    enableParentalCtrlButton.click()
    time.sleep(3)
    setPin()
    time.sleep(3)
    if(wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')))):
        setPin()
        time.sleep(3)

# Disable Parental Control
def disableParentalCtrl():
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'android:id/switch_widget'))
        )
    enableParentalCtrlButton.click()
    time.sleep(3)
    setPin()
    time.sleep(3)
    if(wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')))):
        setPin()
        time.sleep(3)

# Reset Parental Control
def resetParentalCtrl():
    main.scrollDown()
    resetButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Réinitialiser les restrictions")'))
        )
    resetButton.click()
    time.sleep(5)

# Set Parental Control Level
def setParentalCtrlLevel(level):
    tvRatingButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Réinitialiser les restrictions")'))
        )  
    tvRatingButton.click()
    time.sleep(3)

    if level == "Adult":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("18+")'))
            )
        levelButton.click()
        time.sleep(3)

    elif level == "Teen":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(3)

    elif level == "Child":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8+, 13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(3)

    elif level == "All":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("G, 8+, 13+, 16+ et 18+")'))
            )
        levelButton.click()
        time.sleep(3)