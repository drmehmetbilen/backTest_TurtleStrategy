# Backtest Turtle Strategy
This is a simple Python script to backtest the Turtle Trading Strategy for a given list of stocks using historical stock market data. The Turtle Trading Strategy is a classic trend-following trading technique developed in the 1980s. It is designed to capture large price movements by using breakouts from historical highs and lows as entry and exit points. This script implements the Turtle Trading Strategy for long positions.

## Strategy
The script uses the following rules for the Turtle Trading Strategy:

Long entry: When the stock price is higher than the highest price of the past entry_window_size days.
Long exit: When the stock price is lower than the highest price of the past exit_window_size days.
Usage
To use this script, simply run the provided Python code. The script will download historical stock data for the specified tickers and time period using the yfinance library. It will then calculate the Turtle Trading signals and backtest the strategy. Finally, it will print out the trade log and summary for each ticker and export the summary to an Excel file.

```python
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA', 'NVDA', 'NFLX', 'BA', 'DIS']
start_date = '2013-01-01'
end_date = '2023-01-01'
main(tickers, start_date, end_date)
```


You can customize the script by changing the tickers, start_date, and end_date variables to backtest the strategy for other stocks or time periods. You can also modify the windowSizeList variable to test different combinations of entry and exit window sizes.

## Output
The script will print the trade log and summary for each ticker, including:

Date: The date of each trade.
Position: The type of trade (Long).
Entry Price: The entry price for the long position.
Exit Price: The exit price for the long position.
Profit: The profit or loss for each trade.
The script will also print the summary statistics for each ticker, including:

Long Profit: The total profit from all long trades.
Average Long Profit: The average profit per long trade.
Profitable Long Trades: The number of profitable long trades.
The summary statistics will be exported to an Excel file named summary.xlsx.
