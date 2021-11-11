from howitzer.util.trading import *

from datetime import datetime, timezone
import unittest


class TestFoltillaTradingCandle(unittest.TestCase):
    def setUp(self):
        self.test_candle_01_inputs = {"time": "2021-01-01T00:00:00.000Z",
                                      "open": 50, "high": 55, "low": 49, "close": 51, "volume": 10000}
        self.test_candle_01 = Candle(self.test_candle_01_inputs)

    def test_createSimpleCandle_time(self):
        self.assertEqual(self.test_candle_01.time, 1609459200000)

    def test_createSimpleCandle_open(self):
        self.assertEqual(self.test_candle_01.open,
                         self.test_candle_01_inputs["open"])

    def test_createSimpleCandle_high(self):
        self.assertEqual(self.test_candle_01.high,
                         self.test_candle_01_inputs["high"])

    def test_createSimpleCandle_low(self):
        self.assertEqual(self.test_candle_01.low,
                         self.test_candle_01_inputs["low"])

    def test_createSimpleCandle_close(self):
        self.assertEqual(self.test_candle_01.close,
                         self.test_candle_01_inputs["close"])

    def test_createSimpleCandle_volume(self):
        self.assertEqual(self.test_candle_01.volume,
                         self.test_candle_01_inputs["volume"])

    def test_createSimpleCandle_percent(self):
        self.assertEqual(self.test_candle_01.percent,  2)

    def test_createSimpleCandle_diff(self):
        self.assertEqual(self.test_candle_01.diff,  1)

    def test_createSimpleCandle_range(self):
        self.assertEqual(self.test_candle_01.range,  6)

    def test_createSimpleCandle_green(self):
        self.assertEqual(self.test_candle_01.green,  True)

    def test_createSimpleCandle_red(self):
        self.assertEqual(self.test_candle_01.red,  False)

    def test_createSimpleCandle_head(self):
        self.assertEqual(self.test_candle_01.head,  4)

    def test_createSimpleCandle_tail(self):
        self.assertEqual(self.test_candle_01.tail,  1)

    def test_createSimpleCandle_body(self):
        self.assertEqual(self.test_candle_01.body,  1)

    def test_createSimpleCandle_twap(self):
        self.assertAlmostEqual(self.test_candle_01.twap,  51.6666667)

    def test_createSimpleCandle_tr_empty(self):
        self.assertEqual(self.test_candle_01.tr,  6)

    def test_createSimpleCandle_twap_with_data(self):
        c = Candle(self.test_candle_01_inputs, previousClose=48)
        self.assertEqual(c.tr,  7)


class TestFoltillaTradingChart(unittest.TestCase):
    def setUp(self):
        self.test_chart_input = [{"time": "2021-01-01T05:00:00.000Z",
                                 "open": 50, "high": 55, "low": 49, "close": 51, "volume": 10000}]
        self.test_chart = Chart(self.test_chart_input)

    def test_chartMakesSingleCandle(self):
        self.assertEqual(len(self.test_chart.candles), 1)
