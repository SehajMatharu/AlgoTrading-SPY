# backtest.py
class BacktestFramework:
    """Main backtesting framework."""
    
    def __init__(self, data: pd.DataFrame, strategy: BaseStrategy, initial_capital: float = 10000):
        self.data = data
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.results = None
        
    def run_backtest(self) -> pd.DataFrame:
        """Executes the backtest."""
        try:
            # Generate trading signals
            self.results = self.strategy.generate_signals(self.data)
            
            # Calculate portfolio value
            self.results['Returns'] = self.results['Close'].pct_change()
            self.results['Strategy_Returns'] = self.results['Returns'] * self.results['Signal'].shift(1)
            self.results['Portfolio_Value'] = self.initial_capital * (1 + self.results['Strategy_Returns'].cumsum())
            
            return self.results
        except Exception as e:
            logger.error(f"Error during backtest: {str(e)}")
            raise
            
    def get_performance_metrics(self) -> dict:
        """Calculates performance metrics for the backtest."""
        if self.results is None:
            raise ValueError("Must run backtest before calculating metrics")
        return PerformanceMetrics.calculate_metrics(self.results)
