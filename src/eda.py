import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

class EDA:
    def __init__(self, df: pd.DataFrame, date_col='Date', price_col='Price'):
        self.df = df.copy()
        self.date_col = date_col
        self.price_col = price_col
        self._prepare_data()

    def _prepare_data(self):
        self.df[self.date_col] = pd.to_datetime(self.df[self.date_col])
        self.df.set_index(self.date_col, inplace=True)
        self.df.sort_index(inplace=True)
        self.df['Log_Return'] = np.log(self.df[self.price_col]).diff()
        self.df.dropna(inplace=True)

    def plot_price(self):
        plt.figure(figsize=(12, 5))
        plt.plot(self.df.index, self.df[self.price_col])
        plt.title("Brent Oil Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_log_return(self):
        plt.figure(figsize=(12, 5))
        plt.plot(self.df.index, self.df['Log_Return'])
        plt.title("Log Returns of Brent Oil Price")
        plt.xlabel("Date")
        plt.ylabel("Log Return")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def check_stationarity(self, col='Log_Return'):
        result = adfuller(self.df[col].dropna())
        print("ADF Statistic:", result[0])
        print("p-value:", result[1])
        print("Critical Values:")
        for key, value in result[4].items():
            print(f"   {key}: {value}")
        if result[1] < 0.05:
            print("✅ The series is likely stationary.")
        else:
            print("❌ The series is likely non-stationary.")

    def run_all(self):
        self.plot_price()
        self.plot_log_return()
        self.check_stationarity()


if __name__ == "__main__":
    # Replace 'brent_oil_prices.csv' with your actual file path
    file_path = '../data/raw/BrentOilPrices.csv'

    try:
        df = pd.read_csv(file_path)
        eda = EDA(df=df, date_col='Date', price_col='Price')
        eda.run_all()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")