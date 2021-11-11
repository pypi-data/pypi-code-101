from datetime import datetime, timedelta
from howitzer.util.date import shortStringFormat
from os.path import join
import dateutil.parser as dateparse
import ujson as json
import math


class Candle:
    def __init__(self, currentData: dict, previousClose: float = None):
        self.time = round(dateparse.parse(
            currentData["time"]).timestamp() * 1000)
        self.low = currentData["low"]
        self.high = currentData["high"]
        self.open = currentData["open"]
        self.close = currentData["close"]
        self.volume = currentData["volume"]
        self.percent = 100 * (self.close - self.open) / self.open
        self.diff = self.close - self.open
        self.range = self.high - self.low
        self.green = self.close > self.open
        self.red = self.close < self.open
        self.head = self.high - max(self.close, self.open)
        self.tail = min(self.open, self.close) - self.low
        self.body = max(self.close, self.open) - min(self.close, self.open)
        self.twap = (self.close + self.high + self.low) / 3
        self.tr = self.range
        if previousClose is not None:
            self.tr = max(self.range, abs(self.high-previousClose),
                          abs(self.low-previousClose))


class Chart:
    def __init__(this, rawCandleData: list):
        this.candles = []
        number_of_candles_to_parse = len(rawCandleData)
        for i in range(number_of_candles_to_parse):
            if i < number_of_candles_to_parse - 1:
                this.candles.append(
                    Candle(rawCandleData[i], previousClose=rawCandleData[i+1]["close"]))
            if i == number_of_candles_to_parse - 1:
                this.candles.append(Candle(rawCandleData[i]))


def chartFromDataFiles(pathToDataFolder: str, startDate: datetime, endDate: datetime):
    def BLANK_CANDLE():
        return {"time": None, "low": math.inf, "high": -math.inf, "volume": 0}
        # return [None, math.inf, - math.inf, None, None, 0]

    stopTime = endDate.timestamp()
    dailyRawCandles = []
    # todo: add days to queu and tehn deque on multiple threads to get data, sort after the fact
    while(startDate.timestamp() <= stopTime):
        tempDaily = BLANK_CANDLE()
        nextDay = startDate + timedelta(days=1)

        targetFileName = shortStringFormat(startDate) + ".json"
        targetFilePath = join(pathToDataFolder, targetFileName)
        f = open(targetFilePath)

        data = json.load(f)
        # daily logic
        tempDaily["time"] = data[0]["time"]
        tempDaily["open"] = data[0]["open"]
        for minute in data:
            candleTime = dateparse.parse(minute["time"])
            if candleTime.timestamp() < nextDay.timestamp():
                tempDaily["volume"] += minute["volume"]
                tempDaily["close"] = minute["close"]
                tempDaily["high"] = max(tempDaily["high"], minute["high"])
                tempDaily["low"] = min(tempDaily["low"], minute["low"])

        dailyRawCandles.append(tempDaily)
        startDate = nextDay
        f.close()

    dailyRawCandles.reverse()
    return {
        "daily": Chart(dailyRawCandles)
    }
