# brokerbot class

### brokerbot.data(traded_pair)

ohlc data get loaded/updated from a data connector
orderlog is created from buy/sell orders

    brokerbot.data.ohlc_data: Pandas dataframe, OHLC prices
    brokerbot.data.orderlog: Dictionary/JSON, timestamp, BUY or SELL, price, # of units

### brokerbot.strategy


    brokerbot.strategy.buy: strategy used for buying
    brokerbot.strategy.sell: strategy used for selling

