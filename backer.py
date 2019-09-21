import pandas as pd
import pandas_ta as ta
from data_connectors import CryptoWatchREST
from time import sleep
from pprint import PrettyPrinter as pp

import sys

class Strategy:
    def crossed_over(self, series1, series2):
        if series1[-2] <= series2[-2] and series1[-1] > series2[-1]:
            return True
        else:
            return False

class SMAstrategy(Strategy):

    def __init__(self, df):
        try:
            self.sma_long = df.ta.sma(length=30, append=True)
            self.sma_short = df.ta.sma(length=10, append=True)
        except:
            pass


    def decide_action(self):
        try:
            if self.crossed_over(self.sma_short, self.sma_long):
                return 'buy'
            if self.crossed_over(self.sma_long, self.sma_short):
                return 'sell'
            else:
                return 'wait'
        except:
            pass


OHLC_PERIOD = sys.argv[1]

if __name__ == "__main__":
    
    '''
    backer backtesting function
    ===========================
    '''
    df_dict = CryptoWatchREST.get_ohlc('kraken', 'xrp', 'eur', [OHLC_PERIOD])
    df = df_dict[OHLC_PERIOD]
    
    results_dict = {}
    results_df = pd.DataFrame(columns=df.columns)
    results_df['action'] = pd.Series()
    results_df['opt_profit_loss'] = pd.Series()
    results_df['pess_profit_loss'] = pd.Series()

    pos_open = False
    order = 'none'

    for i in range(len(df.index)):
        rolling_df = df.head(i)       

        action = SMAstrategy(rolling_df).decide_action()

        if order == 'buy':
            results_dict[str(rolling_df.index[-1])] = {'action': action, 'price': rolling_df.close[-1]}
            results_df = results_df.append(rolling_df.iloc[-1])
            results_df['action'].iloc[-1] = order
            pos_open = True
            order = 'none'

        elif order == 'sell':
            results_dict[str(rolling_df.index[-1])] = {'action': action, 'price': rolling_df.close[-1]}
            results_df = results_df.append(rolling_df.iloc[-1])
            results_df['action'].iloc[-1] = order
            pos_open = False
            order = 'none'


        if action == 'buy' and pos_open == False:
            order = 'buy'
            # pos_open = True

        elif action == 'sell' and pos_open == True:
            order = 'sell'
            # pos_open = False
        else:
            action = 'wait'

    pp().pprint(results_dict)

    # bilance = 0
    # for key, value in results_dict.items():
    #     if value['action'] == 'buy':
    #         bilance -= float(value['price'])
    #     elif value['action'] == 'sell':
    #         bilance += float(value['price'])
    
    # print('bilance: ', bilance)

    for i in range(len(results_df)):
        if results_df.action.iloc[i] == 'sell':
            results_df['opt_profit_loss'].iloc[i] = results_df.high.iloc[i] - results_df.low.iloc[i-1]
            results_df['pess_profit_loss'].iloc[i] = results_df.low.iloc[i] - results_df.high.iloc[i-1]

    print(results_df)

    print('TOTAL OPT PROFIT/LOSS: %f' % results_df.loc[results_df.action == 'sell']['opt_profit_loss'].sum())
    print('TOTAL PESS PROFIT/LOSS: %f' % results_df.loc[results_df.action == 'sell']['pess_profit_loss'].sum())


    import pdb; pdb.set_trace()