import pprint
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import math
from typing import List, Dict


def daily(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    daily = pd.DataFrame()
    for t in tickers:
        daily[t] = wb.DataReader(t, data_source='yahoo', start=start, end=end)['Adj Close']
    return daily


def annual_returns(daily: pd.DataFrame) -> pd.DataFrame:
    delta = (daily/daily.shift(1)) - 1
    return delta.mean() * 250


def plot_daily(daily: pd.DataFrame) -> None:
    (daily/daily.iloc[0] * 100).plot()
    plt.show()


def daily_log(daily: pd.DataFrame) -> pd.DataFrame:
    return np.log(daily/daily.shift(1))


def risk(daily_log: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    risk = {}
    for ticker,value in daily_log.to_dict().items():
        if ticker not in risk:
            risk[ticker] = {}
        risk[ticker]['daily_mean'] = daily_log[ticker].mean()
        risk[ticker]['annual_mean'] = risk[ticker]['daily_mean'] * 250
        risk[ticker]['daily_std'] = daily_log[ticker].std()
        risk[ticker]['annual_std'] = risk[ticker]['daily_std'] * (250 ** 0.5)
    return risk


if __name__ == "__main__":
    d = daily(['PG', 'BEI.DE'], '2007-01-01', '2020-05-03')
    plot_daily(d)
    ld = daily_log(d)
    print(ld)
    pprint.pprint(risk(ld))
