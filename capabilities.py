from appium.options.android import UiAutomator2Options

class Capability:
    
    def get_android_options(device, app_name):
        appium = UiAutomator2Options()
        appium.platform_name = "Android"
        appium.device_name = device
        appium.automation_name = "UiAutomator2"
        appium.app = None
        
        # Mapping apps
        apps = {
            "helixTv": ("com.videotron.helixtv", "com.xfinity.common.view.LaunchActivity"),
            "helixFi": ("com.videotron.helixfi", "com.xfinity.common.view.LaunchActivity"),
            "illicoPlus": ("com.videotron.illicoplus", "com.xfinity.common.view.LaunchActivity")
        }
        
        if app_name in apps:
            appium.app_package, appium.app_activity = apps[app_name]

        appium.ensure_webviews_have_pages = True
        appium.native_instruments_lib = True
        appium.no_reset = True
        appium.force_app_launch = True
        
        return appium
