#!/usr/bin/env python

from data_connectors import CryptoAlphaVantage

from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from dotenv import load_dotenv
from backtesting.test import SMA, GOOG
from os import environ
import pandas_ta as ta

load_dotenv()
ALPHAVANTAGE_APIKEY = environ['ALPHAVANTAGE_APIKEY']


crypto_data = CryptoAlphaVantage.get_daily(
    'XRP',
    'EUR',
    ALPHAVANTAGE_APIKEY
).drop(
columns=['open_USD','high_USD','low_USD','close_USD','market_cap_USD']
).rename(columns={
'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'
})

import pdb; pdb.set_trace()

class SmaCross(Strategy):
    n1 = 10
    n2 = 30

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


bt = Backtest(crypto_data, SmaCross, cash=10000, commission=.002)

output = bt.run()
bt.plot()
print(output)