#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:06:31 2020

@author: mac
"""


import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams



df = pd. read_csv('airline_passengers.csv',index_col='Month' ,parse_dates=True)



df.info()

'''
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 144 entries, 1949-01-01 to 1960-12-01
Freq: MS
Data columns (total 1 columns):
Thousands of Passengers    144 non-null int64
dtypes: int64(1)
memory usage: 2.2 KB
'''

df.index.freq = 'MS'

training_data = df.iloc[:109]

test_data = df.iloc[108:]


from statsmodels.tsa.holtwinters import ExponentialSmoothing

fitted_model = ExponentialSmoothing(training_data['Thousands of Passengers'],trend = 'mul',seasonal = 'mul',seasonal_periods=12).fit()

test_predictions = fitted_model.forecast(36)



training_data['Thousands of Passengers'].plot(legend=True,label='TRAIN',figsize = (12,5))
test_data['Thousands of Passengers'].plot(legend=True,label='TEST',figsize = (12,5))
test_predictions.plot(legend=True,label='PREDICTION',figsize=(12,5))

