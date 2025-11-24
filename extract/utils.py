import uuid
import base64

from bs4 import Tag

from extract.exceptions import MissingItemFieldError

NONE_TEXT = "N/A"
NONE_MONEY = "$0.0"


def get_text_using(
    tag: Tag,
    selector: str,
    class_name: str = None,
    attrs: dict = None,
    none_str: str = NONE_TEXT,
    raise_if_missing: bool = False,
):
    """
    Get text from a BeautifulSoup Tag using a selector and optional class name or attributes.
    Args: tag (bs4.element.Tag): The BeautifulSoup Tag to search within.
        selector (str): The HTML tag name to search for (e.g., 'div', 'span').
        class_name (str, optional): The class name to filter the search. Defaults to None.
        attrs (dict, optional): Additional attributes to filter the search. Defaults to None.
        none_str (str, optional): The string to return if the tag is not found. Defaults to 'N/A'.
        raise_if_missing (bool, optional): Whether to raise an exception if the tag is not found. Defaults to False.
    Returns:    str: The text content of the found tag, or none_str if not found.
    Raises:    ValueError: If raise_if_missing is True and the tag is not found.
    """
    if class_name:
        found_tag = tag.find(selector, class_=class_name)
    elif attrs:
        found_tag = tag.find(selector, attrs=attrs)
    else:
        found_tag = tag.find(selector)

    if found_tag:
        return found_tag.text.strip()
    else:
        if raise_if_missing:
            raise MissingItemFieldError(selector)
        else:
            return none_str


def short_uuid() -> str:
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip(b"=").decode("ascii")
