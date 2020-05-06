import unittest

import pandas as pd

import utils


class TestDaily(unittest.TestCase):
    def test_one(self):
        data = utils.daily(['PG'], '2000-01-01')
        self.assertAlmostEqual(data['PG'].mean(), 52.1409, places=4)
    def test_many(self):
        data = utils.daily(['F','MSFT'], '2000-01-01')
        self.assertAlmostEqual(data['F'].mean(), 8.8089, places=4)
        self.assertAlmostEqual(data['MSFT'].mean(), 38.1731, places=4)


if __name__ == '__main__':
    unittest.main()
