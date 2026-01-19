from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from helix_navigator import main, home

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)

# Set Parental Control
def setParentalCtrl(pinCode):
    # Go to Home
    main.goToHome()
    time.sleep(5)

    # Go to Profile
    home.goToProfile()
    time.sleep(5)

    # Go to Parental Control
    parentalCtrlSection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(5)'))
        )
    parentalCtrlSection.click()
    time.sleep(5)

    # Set PIN Code
    for digit in pinCode:
        pinButton = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, f'new UiSelector().text("{digit}")'))
            )
        pinButton.click()
        time.sleep(3)
    time.sleep(5)

# Disable Parental Control
def disableParentalCtrl(pinCode):
    # Go to Home
    main.goToHome()
    time.sleep(5)

    # Go to Profile
    home.goToProfile()
    time.sleep(5)

    # Go to Parental Control
    parentalCTRLSection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(5)'))
        )
    parentalCTRLSection.click()
    time.sleep(5)

    # Set PIN Code
    for digit in pinCode:
        pinButton = wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, f'new UiSelector().text("{digit}")'))
            )
        pinButton.click()
        time.sleep(3)
    time.sleep(5)

# Set Parental Control Level (Adult)
def setParentalCtrlLevelAdult():
    levelAdultButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Adult")'))
        )
    levelAdultButton.click()
    time.sleep(5)

# Set Parental Control Level (Teen)
def setParentalCtrlLevelTeen():
    levelTeenButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Teen")'))
        )
    levelTeenButton.click()
    time.sleep(5)

# Set Parental Control Level (Child)
def setParentalCtrlLevelChild():
    levelChildButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Child")'))
        )
    levelChildButton.click()
    time.sleep(5)

# Reset Parental Control
def resetParentalCtrl():
    resetButton = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().text("Reset")'))
        )
    resetButton.click()
    time.sleep(5)