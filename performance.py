# performance.py
class PerformanceMetrics:
    """Calculates various trading performance metrics."""
    
    @staticmethod
    def calculate_metrics(data: pd.DataFrame, risk_free_rate: float = 0.02) -> dict:
        """Calculates key performance metrics."""
        returns = data['Portfolio_Value'].pct_change()
        
        # Annualized return
        total_return = (data['Portfolio_Value'].iloc[-1] / data['Portfolio_Value'].iloc[0]) - 1
        years = (data.index[-1] - data.index[0]).days / 365.25
        annual_return = (1 + total_return) ** (1 / years) - 1
        
        # Sharpe ratio
        excess_returns = returns - risk_free_rate / 252
        sharpe_ratio = np.sqrt(252) * excess_returns.mean() / returns.std()
        
        # Maximum drawdown
        cumulative_returns = (1 + returns).cumprod()
        rolling_max = cumulative_returns.expanding().max()
        drawdowns = cumulative_returns / rolling_max - 1
        max_drawdown = drawdowns.min()
        
        return {
            'Total Return': total_return,
            'Annual Return': annual_return,
            'Sharpe Ratio': sharpe_ratio,
            'Max Drawdown': max_drawdown
        }