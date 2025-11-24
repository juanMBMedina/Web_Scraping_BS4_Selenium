from abc import ABC, abstractmethod
import pandas as pd
from logger import logger


class BaseExtractor(ABC):
    """
    Base class for all web data extractors.
    It provides common utilities and defines the essential parsing interface.
    """

    @staticmethod
    def to_dataframe(objects_list: list) -> pd.DataFrame:
        """
        Converts a list of objects (Items, Instalments, etc.) to a pandas DataFrame.
        This logic is universal for all extractors.
        """
        if not objects_list:
            logger.warning("to_dataframe called with an empty list.")
            return pd.DataFrame()

        logger.info(f"Converting list of {len(objects_list)} objects to DataFrame...")

        try:
            df = pd.DataFrame(objects_list)
            logger.info("DataFrame conversion successful.")
            return df
        except Exception as e:
            logger.error(f"Failed to convert objects to DataFrame: {e}")
            raise

    # ---------------------------------------------------------------
    # ABSTRACT METHODS - MUST BE IMPLEMENTED BY CHILD CLASSES
    # ---------------------------------------------------------------

    @abstractmethod
    def parse(self, html):
        """
        Abstract method: This must be overridden by every child class to
        implement the website-specific HTML parsing logic.
        """
        # The 'pass' here is fine since @abstractmethod handles the enforcement
        pass
