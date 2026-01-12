from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Capabilities & Setup
appium = UiAutomator2Options()
appium.platform_name = "Android"
appium.device_name = "ANDROID NAME (TBD)"
appium.automation_name = "UiAutomator2"
appium.app = "C:/path/to/your/app.apk"  # CHANGE THIS to your APK path
appium.ensure_webviews_have_pages = True
appium.native_instruments_lib = True

# Connect to Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", appium=appium)

try:
    print("Session Started Successfully!")
    
    # Example: Finding an element by Accessibility ID (the best way)
    login_button = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login')
    login_button.click()
    
    # Wait for 5 seconds so you can see it open
    import time
    time.sleep(5)

finally:
    driver.quit()
    print("Session Closed.")