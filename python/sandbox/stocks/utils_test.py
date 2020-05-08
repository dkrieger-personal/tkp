import unittest

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


if __name__ == '__main__':
    unittest.main()
