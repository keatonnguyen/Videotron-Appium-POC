from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import capabilities

# HelixTv Capabilities
options = capabilities.getCapabilities("Pixel 4 XL", "helixTv")

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)



# -------------------------------------------NAVIGATION BAR-------------------------------------------

# Go to Home Section
def goToHome():
    homeSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(8)'))
        )
    homeSection.click()
    time.sleep(10)

# Go to Live TV Section
def goToLiveTV():
    liveTVSection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)'))
        )
    liveTVSection.click()
    time.sleep(10)

# Go to My Library Section
def goToMyLibrary():
    myLibrarySection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(12)'))
        )
    myLibrarySection.click()
    time.sleep(10)

# Go to Search Section
def goToSearch():
    searchSection = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, 'new UiSelector().className("android.view.View").instance(14)'))
        )
    searchSection.click()
    time.sleep(10)



# -------------------------------------------TOOL BAR-------------------------------------------

# Go to Profile Section
def goToProfile():
    goToHome()
    goBack()
    time.sleep(10)

# Go to Airplay
def goToAirplay():
    airplaySection = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Diffuser. Déconnecté")'))
        )
    airplaySection.click()
    time.sleep(10)

# Go to Back
def goBack():
    backButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")'))
        )
    backButton.click()
    time.sleep(10)



# -------------------------------------------LIVE TV-------------------------------------------

# Go to Filter Channels
def goToFilterChannels():
    goToLiveTV()
    filterButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/filters_button'))
        )
    filterButton.click()
    time.sleep(10)

# Go to Date & Time Channels
def goToDateTimeChannels():
    goToLiveTV()
    dateTimeButton = wait.until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.videotron.helixtv:id/date_display'))
        )
    dateTimeButton.click()
    time.sleep(10)

# Go to TVA Channel
def goToTVA():
    goToLiveTV()
    tvaChannel = wait.until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")'))
        )
    tvaChannel.click()
    time.sleep(10)

# Go to Adult Channel
def goToAdultChannel():
    goToLiveTV()
    adultChannel = wait.until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Chaîne : 340. Playboy Enterprises. '))
        )
    adultChannel.click()
    time.sleep(10)

