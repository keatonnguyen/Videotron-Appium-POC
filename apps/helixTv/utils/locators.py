from appium.webdriver.common.appiumby import AppiumBy

class GlobalLocators:
    
    # Navigation Bar
    HOME_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accueil")')
    LIVE_TV_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Télé en direct")')
    MY_LIBRARY_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ma bibliothèque")')
    SEARCH_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Parcourir")')

    # Basic Navigation Buttons
    BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")')


class HomeLocators:
    AIRPLAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Diffuser. Déconnecté")')
    SETTINGS_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Revenir en arrière")')


class LiveTVLocators:
    # Channels
    CHANNEL_4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")')
    CHANNEL_340 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("340")')

    # Filter
    FILTER_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/filters_button")')
    FILTER_FAVORITES_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Chaînes favorites")')
    FILTER_CONFIRM_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/ok_button")')


class SettingsLocators:
    This_DEVICE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Cet appareil :")')
    PLAYBACK_PREFERENCES_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Préférences de lecture")')
    ACCESSIBILITY_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Accessibilité")')
    PARENTAL_CONTROLS_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Contrôle parental")')
    MANAGE_DEVICES_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gérer les appareils")')
    HELP_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Aide")')
    TERMS_OF_USE_SECTION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Conditions d’utilisation")')

    APP_VERSION = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and contains(@text, "Version")]')

class ParentalCtrlLocators:
    # Pin
    PIN_PROMPT = (AppiumBy.ID, 'com.videotron.helixtv:id/pin_prompt_state')
    
    @staticmethod
    def get_pin_digit(digit):
        return (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("com.videotron.helixtv:id/{digit}")')

    PARENTAL_CTRL_TOGGLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/switch_widget")')
    RESET_PARENTAL_CTRL_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Réinitialiser les restrictions")')
    TV_RATING_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Classement d’émission de télévision (français)")')

    # Parental Ctrl Levels
    LEVEL_ADULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("18+")')
    LEVEL_TEEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("13+, 16+ et 18+")')
    LEVEL_CHILD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8+, 13+, 16+ et 18+")')
    LEVEL_ALL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("G, 8+, 13+, 16+ et 18+")')


class EntityLocators:
    PLAY_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/entity_action_text")')
    FAVORITE_BUTTON = (AppiumBy.ID, 'com.videotron.helixtv:id/entity_favorite')
    MORE_OPTIONS_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Plus d'options")


class SearchLocators:
    SEARCH_BOX = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    SEARCH_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/search_src_text")')
    FIRST_RESULT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.videotron.helixtv:id/image_view")')
