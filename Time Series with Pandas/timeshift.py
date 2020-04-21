#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:44:00 2020

@author: mac
"""


import pandas as pd



df = pd.read_csv('starbucks.csv',index_col='Date', parse_dates=True)

df.shift(-1)

df['Close'].plot(figsize=(12,5))


df['Close'].plot(figsize=(12,5))
df.rolling(window=60).mean()['Close'].plot()



df['Close 30 days mean']=df['Close'].rolling(window=60).mean()

#mean of last 7 days



df[['Close','Close 30 days mean']].plot(figsize=(12,5))


df['Close'].expanding().mean().plot(figsize=(12,5))
