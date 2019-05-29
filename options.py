import yfinance as fyf
from pandas_datareader import data as pdr

fyf.pdr_override()

apple = pdr.get_data_yahoo("AAPL", start='2017-01-01')
stock_apple = apple['Close']

stock_apple.head()

