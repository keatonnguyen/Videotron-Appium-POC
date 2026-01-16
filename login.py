from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import capabilities

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    print("Starting Session...")
    wait = WebDriverWait(driver, 5)

    loginButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/get_started_button'))
    )
    loginButton.click()
    wait = WebDriverWait(driver, 5)

    videotronId = wait.until(
    EC.presence_of_element_located((AppiumBy.ID, 'input30'))
    )
    videotronId.send_keys("Trtknguyen@videotron.com")
    wait = WebDriverWait(driver, 5)

    nextButton = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Suivant")'))
    )
    nextButton.click()
    wait = WebDriverWait(driver, 5)

    microsoftId = wait.until(
    EC.presence_of_element_located((AppiumBy.ID, 'input30'))
    )
    microsoftId.send_keys("Trtknguyen@videotron.com")

    microsoftButton = wait.until(
    EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("idSIButton9")'))
    )
    microsoftButton.click()
    wait = WebDriverWait(driver, 5)

    wait = WebDriverWait(driver, 10)


finally:
    driver.quit()
    print("Session Closed.")