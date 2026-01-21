from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from . import main
from functions.action import filter

from helixTv.functions.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4 XL", "helixTv")
driver = get_driver()
wait = get_wait()
short_wait = WebDriverWait(driver, 10)  # 10-second timeout



#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to TVA Channel
def goToTVA():
    foundChannels = False
    while not foundChannels:
        try:
            channel = short_wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")'))
                )
            channel.click()
            foundChannels = True
        except:
            time.sleep(1)
    time.sleep(3)

# Go to Adult Channel
def goToAdultChannel():
    foundChannels = False
    while not foundChannels:
        try:
            channel = short_wait.until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("340")'))
                )
            channel.click()
            foundChannels = True
        except:
            time.sleep(1)
    time.sleep(3)

