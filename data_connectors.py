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

class StockAlphaVantage():
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
        return df

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
        return df


class CryptoAlphaVantage():
    '''
        "Time Series (Digital Currency Daily)": {
        "2019-09-18": {
            "1a. open (CNY)": "72248.58941200",
            "1b. open (USD)": "10187.48000000",
            "2a. high (CNY)": "72456.80759600",
            "2b. high (USD)": "10216.84000000",
            "3a. low (CNY)": "72211.71153200",
            "3b. low (USD)": "10182.28000000",
            "4a. close (CNY)": "72422.83739500",
            "4b. close (USD)": "10212.05000000",
            "5. volume": "466.36058500",
            "6. market cap (USD)": "466.36058500"
        },
    '''

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
        return df
