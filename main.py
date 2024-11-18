if __name__ == "__main__":
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
        
        # Visualize results
        visualizer = Visualizer()
        fig = visualizer.plot_results(results, metrics)
        plt.show()