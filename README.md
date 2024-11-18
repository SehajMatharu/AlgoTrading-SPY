Quantitative Trading Framework

A modular Python framework for backtesting trading strategies, with built-in support for data acquisition, strategy implementation, performance analysis, and visualization.
Features

Data Management: Automated data downloading and preprocessing using yfinance
Strategy Implementation: Flexible strategy pattern for easy implementation of new trading strategies
Performance Analysis: Comprehensive metrics including Sharpe ratio and drawdown calculations
Visualization: Interactive plots for equity curves and trading signals
Error Handling: Robust logging and error management

Installation

Clone the repository:

bashCopygit clone <repository-url>
cd trading-project

Create and activate a virtual environment:

bashCopypython3 -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

Install required packages:

bashCopypip install pandas numpy matplotlib yfinance
Project Structure
Copytrading-project/
├── data_utils.py     # Data downloading and preprocessing
├── strategy.py       # Trading strategy implementations
├── performance.py    # Performance metrics calculations
├── backtest.py      # Main backtesting engine
├── visualization.py  # Results visualization
└── main.py          # Entry point and example usage
Usage

Basic usage with the provided moving average crossover strategy:

pythonCopyfrom data_utils import DataLoader
from strategy import MovingAverageCrossover
from backtest import BacktestFramework

# Initialize components
data_loader = DataLoader("SPY", "2010-01-01", "2023-05-26")
strategy = MovingAverageCrossover(short_window=50, long_window=200)

# Download and preprocess data
data = data_loader.download_data()
if data is not None:
    data = data_loader.preprocess_data(data)
    
    # Run backtest
    backtest = BacktestFramework(data, strategy, initial_capital=10000)
    results = backtest.run_backtest()
    metrics = backtest.get_performance_metrics()

Implementing a custom strategy:

pythonCopyfrom strategy import BaseStrategy

class CustomStrategy(BaseStrategy):
    def generate_signals(self, data):
        # Implement your strategy logic here
        return data
Performance Metrics
The framework calculates several key performance metrics:

Total Return
Annual Return
Sharpe Ratio
Maximum Drawdown

Visualization
The framework provides built-in visualization capabilities:
pythonCopyfrom visualization import Visualizer

visualizer = Visualizer()
fig = visualizer.plot_results(results, metrics)
plt.show()
Contributing

Fork the repository
Create a feature branch: git checkout -b feature-name
Commit your changes: git commit -am 'Add feature'
Push to the branch: git push origin feature-name
Submit a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

yfinance for providing free financial data
pandas and numpy for data processing
matplotlib for visualization capabilities
