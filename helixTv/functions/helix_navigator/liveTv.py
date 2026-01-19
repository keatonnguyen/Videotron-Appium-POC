from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
import main


# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)

# Go to Filter Channels
def goToFilterChannels():
    main.goToLiveTV()
    filterButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/filters_button'))
        )
    filterButton.click()
    time.sleep(10)

# Go to Date & Time Channels
def goToDateTimeChannels():
    main.goToLiveTV()
    dateTimeButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/date_display'))
        )
    dateTimeButton.click()
    time.sleep(10)

# Go to TVA Channel
def goToTVA():
    foundChannels = False
    while not foundChannels:
        main.goToLiveTV()
        if(wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")')))):
            filterButton = wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")'))
                )
            filterButton.click()
            foundChannels = True
        time.sleep(5)
    time.sleep(10)

# Go to Adult Channel
def goToAdultChannel():
    foundChannels = False
    while not foundChannels:
        main.goToLiveTV()
        if(wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chaîne : 340. Playboy Enterprises. ')))):
            filterButton = wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chaîne : 340. Playboy Enterprises. '))
                )
            filterButton.click()
            foundChannels = True
        time.sleep(5)
    time.sleep(10)

