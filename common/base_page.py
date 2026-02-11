from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or self.DEFAULT_TIMEOUT)

    # ---------- Waited finders ----------
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ---------- Actions ----------
    def click(self, locator):
        self.find_clickable(locator).click()

    def type(self, locator, text, clear=True):
        el = self.find_visible(locator)
        if clear:
            el.clear()
        el.send_keys(text)

    # ---------- Reads ----------
    def get_text(self, locator) -> str:
        return self.find_visible(locator).text

    def is_visible(self, locator) -> bool:
        try:
            self.find_visible(locator)
            return True
        except Exception:
            return False

    # ---------- Appium/mobile helpers ----------
    def back(self):
        self.driver.back()