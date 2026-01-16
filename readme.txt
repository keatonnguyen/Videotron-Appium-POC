Setup

1. Download Requirements: pip install -r requirement.typing_extensions

2. Launch Appium: appium

3. Check Devices: adb devices

4. Run test: python login.py


Find packages

1. Search for App: adb shell pm list packages | findstr videotron

2. Get detailed package information: adb shell pm dump com.videotron.helixtv
