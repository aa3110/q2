# IMPORT THE LIBRARY
import yfinance as yf
from datetime import datetime

# CREATE TICKER INSTANCE FOR AMAZON
amzn = yf.Ticker("AMZN")

# GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
end_date = datetime.now().strftime('%Y-%m-%d')
da = amzn.history(start='2022-01-01',end=end_date)

print(da)

da = da.reset_index(drop=False)

da['Date'] = da['Date'].dt.strftime('%Y-%m-%d')

print(da)