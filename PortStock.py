import pandas as pd
import matplotlib.pyplot as plt
key = 'KXRFJKF10FZ75COC'
from alpha_vantage.sectorperformance import SectorPerformances
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

sp = SectorPerformances(key, output_format='pandas')
data, meta_data = sp.get_sector()

data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title("Performance by Sector")
plt.tight_layout()
plt.grid(True)

ta = TechIndicators(key, output_format='pandas')
tsla, meta = ta.get_sma('TSLA', interval='daily', series_type='close')

print(tsla.head)

print(plt.plot(tsla))