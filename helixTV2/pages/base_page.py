from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20) # 20s timeout defined

    # Locate Element
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_condition(locator))

    # Click On Element
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Send Keys
    def type(self, locator, text):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
