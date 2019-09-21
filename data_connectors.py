import requests
import pandas as pd

# Alpha Vantage connection
'''https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo'''

# def stocks_alpha_vantage_get_daily(symbol, outputsize, apikey):
#     r = requests.get(
#         "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=%s&apikey=%s"
#         % (
#             symbol,
#             outputsize,
#             apikey
#         )
#     )
#     df = \
#     pd.DataFrame.from_dict(
#         r.json()["Time Series (Daily)"],
#         orient='index'
#         ).rename(
#             columns={
#                 '1. open': 'open',
#                 '2. high': 'high',
#                 '3. low': 'low',
#                 '4. close': 'close',
#                 '5. volume': 'volume'
#             }
#         )
#     return df
def adjust_dataframe(dataframe):
    '''
    Iterates series in the DF,
    converts them to numerical where possible,
    sorts index to ascending
    '''
    dataframe.index = pd.to_datetime(dataframe.index)
    for column in dataframe.columns:
        try:
            dataframe[column] = pd.to_numeric(dataframe[column])
        except:
            pass
    dataframe.sort_index(ascending=True, inplace=True)

    return dataframe

class StockAlphaVantage:


    @staticmethod
    def get_daily(symbol, outputsize, apikey):
        r = requests.get(
            "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&outputsize=%s&apikey=%s"
            % (
                symbol,
                outputsize,
                apikey
            )
        )
        df = \
        pd.DataFrame.from_dict(
            r.json()["Time Series (Daily)"],
            orient='index'
            ).rename(
                columns={
                    '1. open': 'open',
                    '2. high': 'high',
                    '3. low': 'low',
                    '4. close': 'close',
                    '5. volume': 'volume'
                }
            )
        df = adjust_dataframe(df)
        return df

    @staticmethod
    def get_daily_adjusted(symbol, outputsize, apikey):
        r = requests.get(
            "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=%s&apikey=%s"
            % (
                symbol,
                outputsize,
                apikey
            )
        )
        df = \
        pd.DataFrame.from_dict(
            r.json()["Time Series (Daily)"],
            orient='index'
            ).rename(
                columns={
                    '1. open': 'open',
                    '2. high': 'high',
                    '3. low': 'low',
                    '4. close': 'close',
                    '5. volume': 'volume'
                }
            )
        df = adjust_dataframe(df)
        return df


class CryptoAlphaVantage():
    
    '''
    Static methods for crypto price data on Alpha Vantage
    '''

    @staticmethod
    def get_daily(symbol, market, apikey):
        r = requests.get(
            "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=%s&market=%s&apikey=%s"
            % (
                symbol,
                market,
                apikey
            )
        )
        df = \
        pd.DataFrame.from_dict(
            r.json()["Time Series (Digital Currency Daily)"],
            orient='index'
            ).rename(
                columns={

                    "1a. open (%s)" % market: "open",
                    "1b. open (USD)": "open_USD",
                    "2a. high (%s)" % market: "high",
                    "2b. high (USD)": "high_USD",
                    "3a. low (%s)" % market: "low",
                    "3b. low (USD)": "low_USD",
                    "4a. close (%s)" % market: "close",
                    "4b. close (USD)": "close_USD",
                    "5. volume": "volume",
                    "6. market cap (USD)": "market_cap_USD"
                }
            )
        df = adjust_dataframe(df)
        return df

class CryptoWatchREST:

    # '''
    # https://cryptowat.ch/docs/api
    # Example: https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc

    # Specific periods:

    #     Value	Label
    #     60	1m
    #     180	3m
    #     300	5m
    #     900	15m
    #     1800	30m
    #     3600	1h
    #     7200	2h
    #     14400	4h
    #     21600	6h
    #     43200	12h
    #     86400	1d
    #     259200	3d
    #     604800	1w


    # Example: https://api.cryptowat.ch/markets/coinbase-pro/btcusd/ohlc?periods=86400,300
    
    
    # df.rename(columns={0: 'ts',1: 'o',2: 'h',3: 'l',4: 'c',5: 'unk',6: 'vol'})


    # '''

    @staticmethod
    def get_ohlc(market, crypto, fiat, periods):
        r = requests.get(
            'https://api.cryptowat.ch/markets/%s/%s%s/ohlc?periods=%s' % (
                market,
                crypto,
                fiat,
                ','.join(periods)
            )
        )
        
        df_dict = {}
        
        for item in periods:

            df_dict[item] = pd.DataFrame.from_dict(r.json()['result'][item])
            df_dict[item] = df_dict[item].rename(
                columns={
                        0: 'ts',
                        1: 'open',
                        2: 'high',
                        3: 'low',
                        4: 'close',
                        5: 'volume_%s' % crypto,
                        6: 'volume_%s' % fiat
                    })
            df_dict[item]['ts'] = pd.to_datetime(df_dict[item]['ts'], unit='s')
            df_dict[item] = df_dict[item].set_index('ts')
        
        return df_dict

