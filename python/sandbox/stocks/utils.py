import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import math
from typing import List

def daily(tickers: List[str], start: str) -> pd.DataFrame:
    daily = pd.DataFrame()
    for t in tickers:
        daily[t] = wb.DataReader(t, data_source='yahoo', start=start)['Adj Close']
    return daily

def plot_daily(daily: pd.DataFrame) -> None:
    (daily/daily.iloc[0] * 100).plot()
    plt.show()

if __name__ == "__main__":
    plot_daily(daily(['^GSPC', '^IXIC', '^GDAXI'], '2000-01-01'))
