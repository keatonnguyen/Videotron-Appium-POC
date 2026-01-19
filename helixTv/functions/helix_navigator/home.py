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


# Go to Settings
def goToSettings():
    main.goToHome()
    main.goToBack()
    time.sleep(10)

# Go to Airplay
def goToAirplay():
    main.goToHome()
    airplaySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Diffuser. Déconnecté")'))
        )
    airplaySection.click()
    time.sleep(10)
