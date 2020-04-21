#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:10:27 2020

@author: mac
"""

import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose

import numpy as np

import warnings

warnings.filterwarnings("ignore")

from statsmodels.tsa.statespace.sarimax import SARIMAX

from pmdarima import auto_arima

df = pd.read_csv('co2_mm_mlo.csv')

df['date'] = pd.to_datetime({'year':df['year'], 'month':df['month'], 'day':1})


df.index.freq = 'MS'


df = df.set_index('date')

df.index.freq = 'MS'

df['interpolated'].plot(figsize=(12,5))

result = seasonal_decompose(df['interpolated'],model='add')

result

#uto_arima(df['interpolated'], seasonal = True, m=12)

train = df.iloc[:717]

test = df.iloc[717:]


model = SARIMAX(train['interpolated'], order=(0,1,1),seasonal_order=(1,0,1,12))

results = model.fit()

start= len(train)

end = len(train)+len(test)-1

predictions = results.predict(start,end,typ='level').rename('SARIMA')

test['interpolated'].plot(legend=True, figsize = (12,8))
predictions.plot(legend=True, figsize = (12,8))

from statsmodels.tools.eval_measures import rmse

error = rmse(test['interpolated'],predictions)


test['interpolated'].mean()
predictions.mean()

#forecast unknown future

fcast = results.predict(len(df),len(df)+11, typ='levels').rename('SARIMA Forecast')



df['interpolated'].plot(legend=True,figsize=(12,8))

fcast.plot(legent=True,figsize = (12,8))
