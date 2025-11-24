import pandas as pd
from logger import logger


class CSVLoader:

    @staticmethod
    def save(data: pd.DataFrame, path="output.csv"):
        """
        Saves a pandas DataFrame to a CSV file.
        Args:
            data (pd.DataFrame): DataFrame to save.
            path (str): Path to the output CSV file.
        """
        try:
            data.to_csv(path, index=False)
            logger.info(f"Data successfully saved to {path}")
        except Exception as e:
            logger.error(f"Failed to save data to CSV: {e}")
            raise
