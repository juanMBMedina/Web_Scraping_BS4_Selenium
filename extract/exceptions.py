from logger import logger


class ExtractionError(Exception):
    """
    Base class for extraction-related exceptions.
    """

    pass


class MissingItemFieldError(ExtractionError):
    """
    Exception raised when a critical field (such as title or price)
    is missing in the HTML Tag of an item.
    """

    def __init__(self, field_name: str, message="Missing critical field in HTML tag"):
        self.field_name = field_name
        self.message = f"{message}: {field_name}"
        logger.error(self.message)
        super().__init__(self.message)
