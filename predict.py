#%%
from os import environ
from data_connectors import StockAlphaVantage
from dotenv import load_dotenv
import pandas as pd
from fbprophet import Prophet


load_dotenv()

ALPHAVANTAGE_APIKEY = environ['ALPHAVANTAGE_APIKEY']

hist_price = StockAlphaVantage.get_daily(
    'MSFT',
    'full',
    ALPHAVANTAGE_APIKEY
)

df = \
pd.DataFrame(hist_price).T['4. close'].reset_index()

df = df.rename(columns={'index': 'ds', '4. close': 'y'})

model = Prophet()

model.fit(df)

future = model.make_future_dataframe(periods=365)

forecast = model.predict(future)

import pdb; pdb.set_trace()

#%%
from fbprophet.plot import plot_plotly
import plotly.offline as py
py.init_notebook_mode()

fig = plot_plotly(model, forecast)  # This returns a plotly Figure
py.iplot(fig)

#%%
