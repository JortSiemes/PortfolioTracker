import platform
print('Python version = ' + platform.python_version())
import yfinance as yf
print('yfinance version = ' + yf.__version__)

def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(symbol)
    tickerinfo = tickerdata.info

yfinancetut('TSLA') #Tesla
