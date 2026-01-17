from appium.options.android import UiAutomator2Options

def getCapabilities(device, appName):
    appium = UiAutomator2Options()
    appium.platform_name = "Android"
    appium.device_name = device
    appium.automation_name = "UiAutomator2"
    appium.app = None

    if appName == "helixTv":
        appium.app_package = "com.videotron.helixtv"
        appium.app_activity = "com.xfinity.common.view.LaunchActivity"

    elif appName == "helixFi":
        appium.app_package = "com.videotron.helixfi"
        appium.app_activity = "com.xfinity.common.view.LaunchActivity"

    elif appName == "illicoPlus":
        appium.app_package = "com.videotron.illicoplus"
        appium.app_activity = "com.xfinity.common.view.LaunchActivity"

    appium.ensure_webviews_have_pages = True
    appium.native_instruments_lib = True
    appium.no_reset = True
    return appium
