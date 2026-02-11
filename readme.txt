Download dependencies

    - Download Requirements: pip install -r requirements.txt


Run tests

    Terminal 1:

        Launch Appium: appium

    Terminal 2:

        Check Devices: adb devices

        Run tests: pytest apps/helixTv/tests/test_getversion.py --alluredir=allure-results

        View report: allure serve allure-results


How to find your app:

    Search for App: adb shell pm list packages | findstr videotron

    Get detailed package information: adb shell pm dump com.videotron.helixtv


Project Structure

VIDEOTRON-APPIUM-POC/
├── apps/
│   ├── helixTv  
│   │   ├──pages/
│   │   │   ├──home_page.py     # App page-specific functions
│   │   │   └──...
│   │   │
│   │   ├──utils/
│   │   │   └──locators.py      # Buttons & elements ID for the app
│   │   │
│   │   └──tests/
│   │       ├──conftest.py      # App-specific conftest (specifies app name)
│   │       ├──test_1.py        # Test Case 1 related to app
│   │       └──test_x.py        # Test Cases related to app
│   │
│   └── helixFi
│       └──...                  # Same subdirectories as helixTv
│   
├── common/
│   ├── base_page.py            # Global page functions where all apps inherit from
│   ├── conftest.py             # Global conftest where other conftest inherits from
│   ├── capabilities.py         # App Capabilities
│   └── driver.py               # App Driver
│   
├── config/
│   └── env_config.yaml         # Configurations for Driver & capabilities
│   
├── data/
│   └── user_data.json          # User info for tests
│
├── reports/
│   └── report.html             # Pytest reports
│
├── .gitignore                  # Omits unecessary & unwanted data to project repository
├── app.py                      # Initializes necessary page drivers
├── pytest.ini                  # Pytest Setup
└── requirements.txt            # Project Stack Requirements