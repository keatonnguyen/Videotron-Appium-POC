from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path

# Add paths for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.driver import get_driver, get_wait, initialize_driver
initialize_driver("Pixel 4 XL", "helixTv")
driver = get_driver()
wait = get_wait()

from . import main


#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to Settings
def goToSettings():
    main.goToBack()
    time.sleep(5)

# Go to Airplay
def goToAirplay():
    airplaySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Diffuser. Déconnecté")'))
        )
    airplaySection.click()
    time.sleep(10)
