from os import environ
from data_connectors import StockAlphaVantage
from dotenv import load_dotenv

load_dotenv()

ALPHAVANTAGE_APIKEY = environ['ALPHAVANTAGE_APIKEY']

# hist_price = \
# stocks_alpha_vantage_get_daily(
#     'MSFT',
#     'full',
#     ALPHAVANTAGE_APIKEY
#     )

hist_price_class = StockAlphaVantage.get_daily(
    'MSFT',
    'full',
    ALPHAVANTAGE_APIKEY
)

# print (hist_price)
print (hist_price_class)
import pdb; pdb.set_trace()