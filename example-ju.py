#%%
import pandas as pd
from fbprophet import Prophet
from data_connectors import CryptoAlphaVantage
from data_manglers import ProphetTools
import dotenv
from os import environ

#%%

dotenv.load_dotenv()

ALPHAVANTAGE_APIKEY = environ['ALPHAVANTAGE_APIKEY']


hist_crypto_price = CryptoAlphaVantage.get_daily(
    'XRP',
    'EUR',
    ALPHAVANTAGE_APIKEY
)

df = ProphetTools.prophetify(hist_crypto_price, 'close')


#%%
m = Prophet()
print(dir(m))
m.fit(df)

#%%
future = m.make_future_dataframe(periods=365)
future.tail()

#%%
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

#%%
fig1 = m.plot(forecast)


#%%
fig2 = m.plot_components(forecast)

#%%
from fbprophet.plot import plot_plotly
import plotly.offline as py
py.init_notebook_mode()

fig = plot_plotly(m, forecast)  # This returns a plotly Figure
py.iplot(fig)
