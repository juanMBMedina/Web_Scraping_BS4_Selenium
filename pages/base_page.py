from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import logger  # your colored logger


class BasePage:

    def __init__(self, driver, url: str = None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger

    # ------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------
    def go(self):
        if not self.url:
            raise ValueError("This page does not have an assigned URL.")

        self.logger.info(f"Navigating to URL: {self.url}")
        self.driver.get(self.url)

    # ------------------------------------------------------------
    # Waits
    # ------------------------------------------------------------
    def wait_for_elem_ready(self, locators):
        self.logger.debug(f"Waiting for elements to be visible: {locators}")

        self.wait.until(
            lambda d: (
                len(d.find_elements(*locators)) > 0
                and all(e.is_displayed() for e in d.find_elements(*locators))
            )
        )

        self.logger.info(f"Elements visible: {locators}")

    # ------------------------------------------------------------
    # Generic Actions
    # ------------------------------------------------------------
    def is_displayed(self, locator: By) -> bool:
        """Returns True if the element exists in DOM, False otherwise"""
        try:
            element = self.find(locator)
            return element.is_displayed()
        except:
            self.logger.warning(f"Element not found or not displayed: {locator}")
            return False

    def attribute_contains(self, locator: By, attribute: str, value: str):
        self.logger.debug(
            f"Checking whether attribute '{attribute}' of {locator} contains '{value}'"
        )

        element = self.find(locator)
        attr_value = element.get_attribute(attribute)
        result = value in attr_value

        self.logger.debug(
            f"Attribute value: '{attr_value}' → Contains '{value}': {result}"
        )
        return result

    def find(self, locator: By):
        self.logger.debug(f"Locating element: {locator}")
        elem = self.wait.until(EC.presence_of_element_located(locator))
        self.logger.debug(f"Element located: {locator}")
        return elem

    def clickable(self, locator: By):
        self.logger.debug(f"Waiting for element to be clickable: {locator}")
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        self.logger.debug(f"Element is clickable: {locator}")
        return elem

    def click(self, locator: By):
        self.logger.info(f"Clicking element: {locator}")
        try:
            element = self.clickable(locator)
            element.click()
            self.logger.info(f"Click successful: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element: {locator}", exc_info=True)
            raise

    def send_keys(self, locator: By, text: str):
        self.logger.info(f"Sending keys to {locator}: '{text}'")
        element = self.find(locator)
        element.send_keys(text)

    def scroll_to(self, locator: By):
        self.logger.debug(f"Scrolling to element: {locator}")
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element
        )
        self.logger.debug(f"Scroll completed: {locator}")

    # ------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------
    def get_html(self):
        self.logger.debug("Retrieving page HTML.")
        return self.driver.page_source
