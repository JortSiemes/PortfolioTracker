import pandas as pd
import datetime
import webbrowser
import time
import xlwt

from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

wb = xlwt.Workbook()

ws = wb.add_sheet("TSLA sheet")
print("Excel File Created -bot")

ws.write(0,1,"Ticker")
wb.save("Stock.xls")
print("Excel File Saved -bot")

ts = TimeSeries(key='KXRFJKF10FZ75COC', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='TSLA',interval='1min', outputsize='full')

pprint(data.head(2))

country = data.head

html_content = f"<html> <head> </head> <body> <h1>{country}</h1> </body> </html>"

with open("Port.html", "w") as html_file:
    html_file.write(html_content)

"""df = get_historical_data("KO", output_format="pandas", token=api_key, start=start)

df = df.reindex(index=df.index[::-1])

print(df.head())"""

time.sleep(2)
webbrowser.open_new_tab("Port.html")
