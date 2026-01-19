from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from pages import main, home, settings

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)



# Set PIN
def setPin(pinCode):
    for digit in pinCode:
            pinButton = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'new UiSelector().text("{digit}")'))
                )
            pinButton.click()
            time.sleep(3)
    time.sleep(5)

# Set Parental Control
def setParentalCtrl(pinCode):
    # Go to Parental Control
    main.goToHome()
    time.sleep(5)
    home.goToSettings()
    time.sleep(5)
    settings.goToParentalCtrl()
    time.sleep(5)

    # Turn On Parental Control
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(4)'))
        )
    enableParentalCtrlButton.click()
    time.sleep(5)
    setPin(pinCode)
    main.goToBack()
    time.sleep(5)
    settings.goToDone()
    time.sleep(5)

# Disable Parental Control
def disableParentalCtrl(pinCode):
    # Go to Parental Control
    main.goToHome()
    time.sleep(5)
    home.goToSettings()
    time.sleep(5)
    parentalCTRLSection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(5)'))
        )
    parentalCTRLSection.click()
    time.sleep(5)

    # Reset Parental Control
    setPin(pinCode)
    enableParentalCtrlButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(2)'))
        )
    enableParentalCtrlButton.click()
    setPin(pinCode)
    time.sleep(5)

# Set Parental Control Level
def setParentalCtrlLevel(level, pinCode):
    # Go to Parental Control
    home.goToSettings()
    time.sleep(5)
    settings.goToParentalCtrl()
    time.sleep(5)

    isParentalCtrlSet = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(3)'))
        )
    if isParentalCtrlSet:
        setPin(pinCode)
    time.sleep(5)
    
    # Go to TV ratings
    tvRatingsButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(3)'))
        )
    tvRatingsButton.click()
    time.sleep(5)
    if level == "Adult":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Adult")'))
            )
        levelButton.click()
        time.sleep(5)
    elif level == "Teen":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Teen")'))
            )
        levelButton.click()
        time.sleep(5)
    elif level == "Child":
        levelButton = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Child")'))
            )
        levelButton.click()
        time.sleep(5)
    main.goToBack()
    time.sleep(5)
    main.goToBack()
    time.sleep(5)
    settings.goToDone()
    time.sleep(5)

# Reset Parental Control
def resetParentalCtrl():
    resetButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Reset")'))
        )
    resetButton.click()
    time.sleep(5)