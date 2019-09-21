from os import environ
from data_connectors import StockAlphaVantage, CryptoAlphaVantage, CryptoWatchREST
from dotenv import load_dotenv

load_dotenv()

ALPHAVANTAGE_APIKEY = environ['ALPHAVANTAGE_APIKEY']

# hist_price = \
# stocks_alpha_vantage_get_daily(
#     'MSFT',
#     'full',
#     ALPHAVANTAGE_APIKEY
#     )

# hist_price = StockAlphaVantage.get_daily(
#     'MSFT',
#     'full',
#     ALPHAVANTAGE_APIKEY
# )

df = CryptoAlphaVantage.get_daily(
    'XRP',
    'EUR',
    ALPHAVANTAGE_APIKEY
)

cw_df_dict = CryptoWatchREST.get_ohlc('kraken','btc','eur',['300'])

# print (hist_price)

print(df)

import pdb; pdb.set_trace()


