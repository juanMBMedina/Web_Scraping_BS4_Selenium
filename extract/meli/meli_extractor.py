from bs4 import BeautifulSoup, Tag
from extract.base_extractor import BaseExtractor
from extract.exceptions import MissingItemFieldError
from extract.utils import get_text_using
from extract.meli.models.Item import Item
from extract.meli.models.Instalment import Instalment
from logger import logger
from extract.utils import NONE_MONEY


class MeliExtractor(BaseExtractor):

    # ---------------------------------------------------------------
    # PARSER METHOD
    # ---------------------------------------------------------------

    def parse(self, html: str) -> tuple[list[Item], list[Instalment]]:
        logger.info("Starting HTML parsing using BeautifulSoup...")

        soup = BeautifulSoup(html, "html.parser")
        item_boxes = soup.find_all("li", class_="ui-search-layout__item")

        logger.info(f"Found {len(item_boxes)} items in the page.")

        items = []
        instalments = []

        for index, tag in enumerate(item_boxes):
            try:
                logger.debug(f"Parsing item #{index + 1}...")
                item, inst = self.tag2item(tag)
                items.append(item)
                instalments.append(inst)
            except Exception as e:
                logger.error(f"Failed to parse item #{index + 1}: {e}")

        logger.info(f"Successfully parsed {len(items)} items.")
        return items, instalments

    def tag2item(self, tag: Tag) -> tuple[Item, Instalment]:
        """
        Converts Tag item to MELI Item.
        Args:
            tag (bs4.element.Tag): Tag item to convert.
        Returns:
            Item: MELI Item object.
            Instalment: MELI Instalment object.
        """
        logger.debug("Extracting fields from item tag...")

        title = tag.find("a", class_="poly-component__title")
        if title is None:
            raise MissingItemFieldError("title")

        price_box = tag.find("div", class_="poly-component__price")
        if price_box is None:
            raise MissingItemFieldError("price box")

        current_price_box = price_box.find("div", class_="poly-price__current")
        if current_price_box is None:
            raise MissingItemFieldError("current price")

        last_price = get_text_using(price_box, "s", none_str=NONE_MONEY)
        current_price = get_text_using(
            current_price_box, "span", attrs={"role": "img"}, none_str=NONE_MONEY
        )
        str_installments = get_text_using(
            price_box, "span", class_name="poly-price__installments"
        )

        instalment = Instalment.from_text(str_installments)
        item = Item(title.text, title["href"], last_price, current_price, instalment.id)
        logger.debug(f"Item extracted: {item} | instalment: {instalment}")

        return item, instalment
