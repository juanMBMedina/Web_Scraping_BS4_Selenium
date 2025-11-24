from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from logger import logger


class MeliPage(BasePage):

    URL = "https://www.mercadolibre.com.co/"
    # HEADER
    SEARCH_INPUT = (By.ID, "cb1-edit")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.nav-search-btn")
    # ITEMS
    ITEM_LIST = (By.CSS_SELECTOR, "li.ui-search-layout__item")
    # FOOTER
    CHECK_DIS_BUTTON_STATUS = ("class", "disabled")
    PAGINATION = (By.CSS_SELECTOR, "ul.ui-search-andes-pagination")
    BACK_PAGE_BUTTON = (By.CSS_SELECTOR, "li.andes-pagination__button--back")
    CURRENT_PAGE = (By.CSS_SELECTOR, "li.andes-pagination__button--current")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "li.andes-pagination__button--next")

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def search(self, text):
        self.send_keys(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)
        self.wait_for_elem_ready(self.ITEM_LIST)

    def go_to_page_using_buttons(self, locator) -> bool:
        self.wait_for_elem_ready(self.ITEM_LIST)
        self.get_current_page_number()
        if not self.is_displayed(self.PAGINATION):
            logger.warning("Pagination section not found.")
            return False
        self.scroll_to(self.PAGINATION)
        if not self.is_displayed(locator):
            logger.warning(f"Button with locator {locator} not found.")
            return False
        attr, value = self.CHECK_DIS_BUTTON_STATUS
        # The system can not find the value disable on the attribute class
        is_enable = not self.attribute_contains(locator, attr, value)
        logger.info(f"Button enabled status for {locator}: {is_enable}")
        if is_enable:
            self.wait_for_elem_ready(locator)
            self.click(locator)
            self.wait_for_elem_ready(self.ITEM_LIST)
        return is_enable

    def go_to_next_page(self) -> bool:
        return self.go_to_page_using_buttons(self.NEXT_PAGE_BUTTON)

    def go_to_current_page(self) -> bool:
        return self.go_to_page_using_buttons(self.CURRENT_PAGE)

    def go_to_previous_page(self) -> bool:
        return self.go_to_page_using_buttons(self.BACK_PAGE_BUTTON)

    def get_current_page_number(self) -> int:
        current_page_elem = self.find(self.CURRENT_PAGE)
        page_number = int(current_page_elem.text)
        logger.info(f"Current page number: {page_number}")
        return page_number
