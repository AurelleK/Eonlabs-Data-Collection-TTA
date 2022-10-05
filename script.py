#Eonlabs-Data-Collection-TTA
# by Aurelle TCHAGNA KOUANOU (tkaurelle@gmail.com)
# to run this scrpt, type in your console: python script.py

from pytrends.request import TrendReq
from datetime import datetime
from pytrends import dailydata
import pandas as pd


pytrends = TrendReq(hl='en-US', tz=360)
keywords=['bitcoin']

def hourly():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    timeframe='2015-01-01 '+date
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe)
    data=pytrends.get_historical_interest(keywords, year_start=2015, month_start=1, day_start=1, hour_start=0, year_end=now.year, month_end=now.month, day_end=now.day, hour_end=now.hour, cat=0, geo='', gprop='', sleep=0)
    data = data.reset_index() 
    data.to_csv('data-hour.csv',index=False)
    print('Hourly data collected')


def daily():
    now = datetime.now()
    data = dailydata.get_daily_data('bitcoin', 2015, 1, now.year, now.month)
    data = data.reset_index() 
    data.to_csv('data-day.csv',index=False)
    print(data)


def weekly():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    timeframe='2019-01-02 '+date
    pytrends.build_payload(keywords, cat=0, timeframe='2015-01-01 2019-01-01', geo='', gprop='')
    data1=pytrends.interest_over_time()
    data1 = data1.reset_index()
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='', gprop='') 
    data2=pytrends.interest_over_time()
    data2 = data2.reset_index()
    frame=[data1,data2]
    data=pd.concat(frame)
    data.to_csv('data-week.csv',index=False)
    print(data)

hourly()
daily()
weekly()
