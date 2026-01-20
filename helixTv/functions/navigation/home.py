from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
from pathlib import Path

# Add paths for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helixTv.functions.driver import get_driver, get_wait
driver = get_driver()
wait = get_wait()

from . import main


#//////////////////////////////////////////////////////////////////////////////////////////////

# Go to Settings
def goToSettings():
    main.goToHome()
    time.sleep(5)
    main.goToBack()
    time.sleep(5)

# Go to Airplay
def goToAirplay():
    main.goToHome()
    airplaySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Diffuser. Déconnecté")'))
        )
    airplaySection.click()
    time.sleep(10)
