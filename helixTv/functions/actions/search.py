from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import capabilities
from pages import main

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)

from helixTv.functions.driver import get_driver, get_wait
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Search for a content
def searchContent(contentName):
    main.goToSearch()
    searchBox = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'Search'))
        )
    searchBox.click()
    time.sleep(3)   
    searchBox.send_keys(contentName)
    time.sleep(3)
    firstResult = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/image_view'))
        )
    firstResult.click()
    time.sleep(3)

