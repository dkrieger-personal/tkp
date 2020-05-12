import pprint
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import math
from typing import List, Dict
from scipy import stats
import statsmodels.api as sm


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


def correlation(daily_log: pd.DataFrame) -> pd.DataFrame:
    return daily_log.corr()


def covariance(daily_log: pd.DataFrame) -> pd.DataFrame:
    return daily_log.cov() * 250


def risk(daily_log: pd.DataFrame) -> Dict[str, pd.core.series.Series]:
    risk = {}
    tickers = []
    for ticker, v in daily_log.to_dict().items():
        tickers.append(ticker)
    risk['daily_mean'] = daily_log[tickers].mean()
    risk['annual_mean'] = risk['daily_mean'] * 250
    risk['daily_std'] = daily_log[tickers].std()
    risk['annual_std'] = risk['daily_std'] * (250 ** 0.5)
    return risk


def portfolio(daily_log: pd.DataFrame, weights: np.array) -> (float, float, float, float):
    var = np.dot(weights.T, np.dot(daily_log.cov() * 250, weights))
    vol = var ** 0.5

    r = risk(daily_log)

    mean = np.dot(r['annual_mean'], weights)

    dr = var - np.dot(r['annual_std'] ** 2, np.array([w ** 2 for w in weights]))
    return mean, vol, dr, var - dr


def linear_regression(X: pd.Series, Y: pd.Series) -> (float, float, float):
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    return [intercept, slope, r_value ** 2]

def plot_lr(X: pd.Series, Y: pd.Series, xlabel, ylabel) -> None:
    # scale plot to 110% of max values
    maxX = np.max(X) * 1.1
    maxY = np.max(Y) * 1.1

    intercept, slope, rvalue = linear_regression(X, Y)

    # show raw data
    plt.scatter(X, Y)
    plt.axis([0, maxX, 0, maxY])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # add in regression line
    x_points = [0, maxX]
    y_points = [intercept, intercept + slope * maxX]
    plt.plot(x_points, y_points, marker='x')
    plt.annotate("R2="+str(rvalue), (maxX * 0.1, maxY * 0.9))

    plt.show()


if __name__ == "__main__":
    housing = pd.read_excel(r'C:\Users\David\code\udemy\pyfi\stock\81 Running a Regression in Python\Python 3\Housing.xlsx')

    xlabel = 'House Size (sq.ft.)'
    ylabel = 'House Price'
    X = housing[xlabel]
    Y = housing[ylabel]

    plot_lr(X, Y, xlabel, ylabel)
