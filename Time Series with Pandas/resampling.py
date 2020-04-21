#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:23:05 2020

@author: mac
"""

import pandas as pd

df = pd.read_csv('starbucks.csv',index_col='Date', parse_dates=True)



#daily data ====== yearly data



#https://towardsdatascience.com/using-the-pandas-resample-function-a231144194c4


df.resample(rule='A').mean()


def first_day(entry):
    if len(entry) !=0:
        return entry[0]
    

df.resample(rule='A').apply(first_day)


df['Close'].resample('M').max().plot.bar(figsize=(16,6))



    
