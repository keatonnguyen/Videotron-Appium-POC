import pytest

def getVersionTest(helix_app):
    helix_app.HomePage.go_to_settings()
    helix_app.Settings.check_version()
    print("Version is: " + helix_app.Settings.check_version().text)

