Setup

1. Download Requirements: pip install -r requirements.txt

2. Launch Appium: appium

3. Check Devices: adb devices

4. Run tests: pytest tests/test_x.py --alluredir=allure-results

5. View report: allure serve allure-results


Find packages

1. Search for App: adb shell pm list packages | findstr videotron

2. Get detailed package information: adb shell pm dump com.videotron.helixtv
