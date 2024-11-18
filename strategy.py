# strategy.py
import numpy as np
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    """Abstract base class for trading strategies."""
    
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        pass

class MovingAverageCrossover(BaseStrategy):
    """Implements a simple moving average crossover strategy."""
    
    def __init__(self, short_window: int = 50, long_window: int = 200):
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generates trading signals based on MA crossover."""
        data = data.copy()
        data[f'{self.short_window}_SMA'] = data['Close'].rolling(window=self.short_window).mean()
        data[f'{self.long_window}_SMA'] = data['Close'].rolling(window=self.long_window).mean()
        data['Signal'] = np.where(data[f'{self.short_window}_SMA'] > data[f'{self.long_window}_SMA'], 1, 0)
        data['Position'] = data['Signal'].diff()
        return data