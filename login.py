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
    wait = WebDriverWait(driver, 15)

    loginButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/get_started_button'))
    )
    loginButton.click()
    wait = WebDriverWait(driver, 15)

    nextButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Suivant")'))
    )
    nextButton.click()
    wait = WebDriverWait(driver, 15)

    passwordButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CHOISIR").instance(1)'))
    )
    passwordButton.click()
    wait = WebDriverWait(driver, 15)

    passwordField = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("input111")'))
    )
    passwordField.send_keys("V!deotron1234")
    wait = WebDriverWait(driver, 15)

    passwordValidate = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("VÉRIFIER")'))
    )   
    passwordValidate.click()
    wait = WebDriverWait(driver, 20)

    profileSelect = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")'))
    )
    profileSelect.click()
    wait = WebDriverWait(driver, 15)

    rdkversion = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Version 8.13.0.2846")'))
    )
    print("RDK Version Found: ", rdkversion.text)

    logoutButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Fermer la session")'))
    )
    logoutButton.click()
    wait = WebDriverWait(driver, 15)

    confirmLogout = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/ok_btn")'))
    )
    confirmLogout.click()
    wait = WebDriverWait(driver, 15)

finally:
    driver.quit()
    print("Session Closed.")