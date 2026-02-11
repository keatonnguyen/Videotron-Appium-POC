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
