from appium.webdriver.common.appiumby import AppiumBy

class TaskbarLocators:
    OVERVIEW_ICON = (AppiumBy.ID, "com.videotron.helixfi:id/overview_icon")
    WIFI_ICON = (AppiumBy.ID, "com.videotron.helixfi:id/wifi_icon")
    HOME_ICON = (AppiumBy.ID, "com.videotron.helixfi:id/home_icon")
    ACCOUNT_ICON = (AppiumBy.ID, "com.videotron.helixfi:id/account_icon")

    BACK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
    CANCEL_BUTTON = (AppiumBy.ID, "com.videotron.helixfi:id/cancel_button")


class OverviewLocators:
    SEARCH_BUTTON = (AppiumBy.ID, "com.videotron.helixfi:id/search_button")

    # Top Cards
    SHARE_WIFI_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/share_wifi_card")
    RESTART_GATEWAY_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/restart_gateway_card")
    ADVANCED_SECURITY_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/advanced_security_card")

    ACTIVATE_GATEWAY_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/activate_gateway_card")
    TEST_CONNECTION_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/test_connection_card")
    PODS_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/pods_card")
    HELP_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/help_card")
    HELIXTV_CARD = (AppiumBy.ID, "com.videotron.helixfi:id/helix_tv_card")
