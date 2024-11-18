# data_utils.py
import yfinance as yf
import pandas as pd
from typing import Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader:
    """Handles data downloading and preprocessing for the trading framework."""
    
    def __init__(self, symbol: str, start_date: str, end_date: str):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        
    def download_data(self) -> Optional[pd.DataFrame]:
        """Downloads historical data using yfinance."""
        try:
            logger.info(f"Downloading data for {self.symbol}")
            data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if data.empty:
                logger.error("No data downloaded")
                return None
            return data
        except Exception as e:
            logger.error(f"Error downloading data: {str(e)}")
            return None
            
    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """Preprocesses the downloaded data."""
        data = data.copy()
        data.index = pd.to_datetime(data.index)
        data = data.fillna(method='ffill')
        return data