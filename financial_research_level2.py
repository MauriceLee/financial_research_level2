import pandas as pd
from pandas_datareader import data
import fix_yahoo_finance as yf
yf.pdr_override()
import matplotlib.pyplot as plt
import datetime as dt

start = dt.datetime(2018, 1, 1)
end = dt.datetime.now()
dji = data.get_data_yahoo(['^DJI'], start, end)
twii = data.get_data_yahoo(['^TWII'], start, end)

stocks = pd.DataFrame({"^DJI": dji['Close'].pct_change().cumsum(), "^TWII": twii["Close"].pct_change().cumsum()})

DJI = stocks['^DJI'].plot(color='Blue', label='DJI')
TWII = stocks['^TWII'].plot(color='Red', label='TWII')
plt.show()