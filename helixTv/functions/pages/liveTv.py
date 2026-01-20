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

from helixTv.functions.driver import get_driver, get_wait
driver = get_driver()
wait = get_wait()



#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to TVA Channel
def goToTVA():
    foundChannels = False
    while not foundChannels:
        main.goToLiveTV()
        if(wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chaîne : 3. Télé-Québec (Société de télédiffusion du Québec). ')))):
            filterButton = wait.until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chaîne : 3. Télé-Québec (Société de télédiffusion du Québec). '))
                )
            filterButton.click()
            foundChannels = True
        time.sleep(3)
        main.scrollDown()
    time.sleep(3)

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
        time.sleep(3)
        main.scrollDown()
    time.sleep(3)

