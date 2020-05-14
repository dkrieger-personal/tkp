import unittest

import numpy as np
import pandas as pd

import utils


class TestDaily(unittest.TestCase):
    start = '2000-01-01'
    end = '2020-05-03'

    def test_one(self):
        data = utils.daily(['PG'], TestDaily.start, TestDaily.end)
        self.assertAlmostEqual(data['PG'].mean(), 52.3069, places=4)

    def test_many(self):
        data = utils.daily(['F','MSFT'], TestDaily.start, TestDaily.end)
        self.assertAlmostEqual(data['F'].mean(), 8.4186, places=4)
        self.assertAlmostEqual(data['MSFT'].mean(), 38.0895, places=4)

    def test_annual(self):
        annual = utils.annual_returns(utils.daily(['F', 'MSFT'], TestDaily.start, TestDaily.end))
        self.assertAlmostEqual(annual['F'], 0.0335, places=4)
        self.assertAlmostEqual(annual['MSFT'], 0.1229, places=4)

    def test_risk(self):
        daily = utils.daily(['PG', 'BEI.DE'], '2007-01-01', '2020-05-03')
        actual = utils.risk(utils.daily_log(daily))

        actual1 = actual['annual_mean']
        expected = pd.Series([0.074225, 0.059778], index=['PG', 'BEI.DE'])
        for ticker, value in expected.items():
            self.assertTrue(ticker in actual1)
            self.assertAlmostEqual(actual1[ticker], value, places=5)

        actual1 = actual['annual_std']
        expected = pd.Series([0.18887, 0.21762], index=['PG', 'BEI.DE'])
        for ticker, value in expected.items():
            self.assertTrue(ticker in actual1)
            self.assertAlmostEqual(actual1[ticker], value, places=5)

    def test_covariance(self):
        daily = utils.daily(['PG', 'BEI.DE'], '2007-01-01', '2020-05-03')
        actual = utils.covariance(utils.daily_log(daily))

        expected_PG = pd.Series([0.035671, 0.011251], index=['PG', 'BEI.DE'])
        actual_PG = actual['PG']
        for ticker, value in expected_PG.items():
            self.assertTrue(ticker in actual_PG)
            self.assertAlmostEqual(actual_PG[ticker], value, places=5)

        expected_BEI = pd.Series([0.011251, 0.047357], index=['PG', 'BEI.DE'])
        actual_BEI = actual['BEI.DE']
        for ticker, value in expected_BEI.items():
            self.assertTrue(ticker in actual_BEI)
            self.assertAlmostEqual(actual_BEI[ticker], value, places=5)

    def test_correlation(self):
        daily = utils.daily(['PG', 'BEI.DE'], '2007-01-01', '2020-05-03')
        actual = utils.correlation(utils.daily_log(daily))

        expected_PG = pd.Series([1.0, 0.27339], index=['PG', 'BEI.DE'])
        actual_PG = actual['PG']
        for ticker, value in expected_PG.items():
            self.assertTrue(ticker in actual_PG)
            self.assertAlmostEqual(actual_PG[ticker], value, places=5)

        expected_BEI = pd.Series([0.27339, 1.0], index=['PG', 'BEI.DE'])
        actual_BEI = actual['BEI.DE']
        for ticker, value in expected_BEI.items():
            self.assertTrue(ticker in actual_BEI)
            self.assertAlmostEqual(actual_BEI[ticker], value, places=5)

    def test_portfolio(self):
        d = utils.daily(['PG', 'BEI.DE'], '2010-01-01', '2020-05-07')
        (mean, vol, dr, ndr) = utils.portfolio(utils.daily_log(d), np.array([0.5, 0.5]))
        self.assertAlmostEqual(mean, .088128, places=5)
        self.assertAlmostEqual(vol, 0.14467, places=5)
        self.assertAlmostEqual(dr, 0.00435, places=5)
        self.assertAlmostEqual(ndr, 0.016575, places=5)

    def test_beta(self):
        b = utils.beta('PG', '^GSPC', '2012-01-01', '2016-12-31')
        self.assertAlmostEqual(b, 0.61596, places=5)

    def test_CAPM(self):
        b = utils.beta('PG', '^GSPC', '2012-01-01', '2016-12-31')
        capm = utils.CAPM_return(b, 0.025, 0.075)
        self.assertAlmostEqual(capm, 0.055798, places=5)

if __name__ == '__main__':
    unittest.main()
