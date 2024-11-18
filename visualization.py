import matplotlib.pyplot as plt

class Visualizer:
    """Handles visualization of backtest results."""
    
    @staticmethod
    def plot_results(results: pd.DataFrame, metrics: dict):
        """Plots equity curve and key metrics."""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [2, 1]})
        
        # Plot portfolio value
        results['Portfolio_Value'].plot(ax=ax1, label='Portfolio Value')
        ax1.set_title('Backtest Results')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Portfolio Value')
        ax1.grid(True)
        
        # Plot moving averages
        results['50_SMA'].plot(ax=ax2, label='50-day SMA')
        results['200_SMA'].plot(ax=ax2, label='200-day SMA')
        results['Close'].plot(ax=ax2, label='Price', alpha=0.5)
        ax2.set_title('Moving Averages')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Price')
        ax2.grid(True)
        ax2.legend()
        
        # Add metrics as text
        metrics_text = '\n'.join([f'{k}: {v:.2%}' for k, v in metrics.items()])
        plt.figtext(0.02, 0.02, metrics_text, fontsize=10, ha='left')
        
        plt.tight_layout()
        return fig
