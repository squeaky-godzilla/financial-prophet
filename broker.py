import pandas as pd
import pandas_ta as ta
from data_connectors import CryptoWatchREST
from time import sleep

class Strategy:
    def crossed_over(self, series1, series2):
        if series1[-2] <= series2[-2] and series1[-1] > series2[-1]:
            return True
        else:
            return False

class SMAstrategy(Strategy):

    def __init__(self, df):
        self.sma_long = df.ta.sma(length=30, append=True)
        self.sma_short = df.ta.sma(length=10, append=True)


    def decide_action(self):
        if self.crossed_over(self.sma_short, self.sma_long):
            return 'buy'
        elif self.crossed_over(self.sma_short, self.sma_long):
            return 'sell'
        else:
            return 'wait'
    




if __name__ == "__main__":
    
    '''
    broker main function
    ====================

    flow:
    - get price data
    - calculate indicators
    - {calculate prediction}
    - apply strategies
    - {read technicals summary from web}
    - decide to buy, sell, or wait
    - {execute order on Kraken}
    - wait

    '''
    while True:
        df_dict = CryptoWatchREST.get_ohlc('kraken', 'xrp', 'eur', ['300'])
        df = df_dict['300']
        action = SMAstrategy(df).decide_action()

        if action == 'buy':
            print(10*'=',"{ BUY NOW !!! }",10*'=')
            print(df.tail)

        elif action == 'sell':
            print(10*'=',"{ SELL NOW !!! }",10*'=')
            print(df.tail)
        
        sleep(300)