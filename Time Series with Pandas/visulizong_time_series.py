#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:57:54 2020

@author: mac
"""


import pandas as pd


from matplotlib import dates




df = pd.read_csv('starbucks.csv',index_col='Date', parse_dates=True)



#df.index = pd.to_datetime(df.index)



df['Volume'].plot()


df['Close']['2017-01-01':'2017-12-31'].plot(figsize=(12,5),ylim=[40,70],ls='--',c='red')






ax = df['Close'].plot(xlim=['2017-01-01','2017-03-31'],ylim=[50,60])

ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))

ax.xaxis.set_major_formatter(dates.DateFormatter('%d'))

ax.xaxis.set_minor_formatter(dates.DateFormatter('\n\n%b'))

ax.xaxis.set_minor_locator(dates.MonthLocator())

ax.yaxis.grid(True)




 

