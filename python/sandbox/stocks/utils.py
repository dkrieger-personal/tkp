import pprint
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import math
from typing import List, Dict
from scipy import stats
from scipy.stats import norm
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


def variance(daily_log: pd.DataFrame) -> pd.DataFrame:
    return daily_log.var() * 250


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

def multivariate_regression(Xs: pd.Series, Y: pd.Series):
    X1 = sm.add_constant(Xs)
    lr = sm.OLS(Y, X1).fit()
    print(lr.summary())

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

def efficient_frontier(tickers: List[str], start: str, end: str) -> (np.array, np.array):
    returns = []
    volatilities = []

    dl = daily_log(daily(tickers, start, end))

    for x in range(1000):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)

        (mean, vol, dr, ndr) = portfolio(dl, weights)
        returns.append(mean)
        volatilities.append(vol)

    return np.array(returns), np.array(volatilities)

def efficient_frontier_plot(returns: np.array, volatilities: np.array):
    ef = pd.DataFrame({'Return': returns, 'Volatility': volatilities})
    ef.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6))
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.axis([np.min(volatilities), np.max(volatilities), np.min(returns), np.max(returns)])
    plt.show()


def CAPM(stock: str, benchmark: str, risk_free: float, market_return: float,
         start: str, end: str) -> (float, float, float):
    d_log = daily_log(daily([stock, benchmark], start, end))
    cov_annual = covariance(d_log)
    cov_with_market = cov_annual.iloc[0, 1]
    var_annual = variance(d_log)
    market_var = var_annual[benchmark]
    r = risk(d_log)
    stock_std = r['annual_std'][stock]

    beta = cov_with_market / market_var
    capm = risk_free + beta * (market_return - risk_free)
    sharpe = (capm - risk_free)/stock_std

    return beta, capm, sharpe


def monty_carlo(ticker: str, start: str, end: str, t_intervals: int, iterations: int) -> (np.array,List[float]):
    data = daily([ticker], start, end)
    log_returns = np.log(1 + data.pct_change())
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stddev = log_returns.std()
    daily_returns = np.exp(drift.values + stddev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
    S0 = data.iloc[-1]
    price_list = np.zeros_like(daily_returns)
    price_list[0] = S0
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
    final_price = []
    for i in range(iterations):
        final_price.append(price_list[999][i])
    return price_list, final_price


if __name__ == "__main__":
    mc, final_price = monty_carlo('FB', '2015-01-01', '2020-05-14', 1000, 100)
    pprint.pprint(sorted(final_price))
    plt.hist(final_price, bins=20)
    plt.show()

