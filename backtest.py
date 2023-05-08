import pandas as pd
import numpy as np
import yfinance as yf

def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def turtle_trading(data, entry_window_size=50, exit_window_size=20):
    data['high'] = data['High'].rolling(window=entry_window_size).max()
    data['low'] = data['Low'].rolling(window=entry_window_size).min()
    data['exit_high'] = data['High'].rolling(window=exit_window_size).max()
    data['long_entry'] = data['Close'] > data['high'].shift(1)
    data['long_exit'] = data['Close'] < data['exit_high'].shift(1)
    return data

def backtest_turtle_strategy(ticker, start_date, end_date, entry_window_size, exit_window_size):
    data = get_data(ticker, start_date, end_date)
    turtle_data = turtle_trading(data, entry_window_size, exit_window_size)

    position = 0
    entry_price = 0
    trade_log = []

    for index, row in turtle_data.iterrows():
        if row['long_entry'] and position <= 0:
            position = 1
            entry_price = row['Close']
            trade_type = 'Long'

        elif row['long_exit'] and position > 0:
            position = 0
            exit_price = row['Close']
            profit = exit_price - entry_price
            trade_log.append((index, 'Long', entry_price, exit_price, profit))

        else:
            continue

    return trade_log

def print_trade_log(trade_log):
    print("Date\t\tPosition\tEntry Price\tExit Price\tProfit")
    print("-" * 65)
    for trade in trade_log:
        date, trade_type, entry_price, exit_price, profit = trade
        print(f"{date:%Y-%m-%d}\t{trade_type}\t{entry_price:.2f}\t\t{exit_price:.2f}\t\t{profit:.2f}")

def trade_summary(ticker, trade_log, entry_window_size, exit_window_size):
    long_trades = [trade for trade in trade_log if trade[1] == 'Long']

    long_profit = sum(trade[4] for trade in long_trades)
    long_count = len(long_trades)

    avg_long_profit = long_profit / long_count if long_count > 0 else 0

    profitable_long_trades = sum(1 for trade in long_trades if trade[4] > 0)

    return {
        'ticker': ticker,
        'long_profit': long_profit,
        'avg_long_profit': avg_long_profit,
        'profitable_long_trades': profitable_long_trades,
        'Entry Window': entry_window_size,
        'Exit Window': exit_window_size
    }

def print_summary(summary):
    print("\nSummary:")
    print("-" * 40)
    print(f"Long Profit: {summary['long_profit']:.2f}")
    print(f"Average Long Profit: {summary['avg_long_profit']:.2f}")
    print(f"Profitable Long Trades: {summary['profitable_long_trades']}")

def main(tickers, start_date, end_date):
    summary_list = []
    windowSizeList = [(20, 10), (50, 20), (100, 50), (200, 100)]
    for entry_window_size, exit_window_size in windowSizeList:
        for ticker in tickers:
            trade_log = backtest_turtle_strategy(ticker, start_date, end_date, entry_window_size, exit_window_size)
            summary = trade_summary(ticker, trade_log,entry_window_size, exit_window_size)
            summary_list.append(summary)
            print(f"\n{ticker} Trade Log:")
            print_trade_log(trade_log)
            print_summary(summary)
        df = pd.DataFrame(summary_list)
        df.to_excel('summary.xlsx')


tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA', 'NVDA', 'NFLX', 'BA', 'DIS']
start_date = '2013-01-01'
end_date = '2023-01-01'

main(tickers, start_date, end_date)
