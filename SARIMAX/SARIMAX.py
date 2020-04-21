#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:49:06 2020

@author: mac
"""

import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose

import numpy as np

import warnings

warnings.filterwarnings("ignore")

from statsmodels.tsa.statespace.sarimax import SARIMAX

from pmdarima import auto_arima

df = pd.read_csv('RestaurantVisitors.csv',index_col ='date',parse_dates=True)

df.index.freq = 'D'

df1 = df.dropna()

df1.tail()

cols = ['rest1', 'rest2', 'rest3','rest4', 'total']

for column in cols:
    df1[column] = df1[column].astype(int)
    
ax = df1['total'].plot(figsize=(16,5))

for day in df1.query('holiday==1').index:
    ax.axvline(x=day,color='black',alpha=0.8);
    

auto_arima(df1['total'], exogenous = df1[['holiday']], seasonal=True, m=7).summary()

 
#TRAIN SARIMAX Model

train = df1[:400]

test = df1[400:]

model = SARIMAX(train['total'],exog=train[['holiday']], order=(1,0,1), seasonal_order=(1,0,1,7), enforce_invertibility= False)

result = model.fit()
  
start = len(train)

end = len(train) + len(test) -1

predictions = result.predict(start,end,exog=test[['holiday']]).rename('SARIMAX with Exogoneous')

predictions.plot(figsize=(12,7),legend=True)

ax = test['total'].plot(figsize=(12,7),legend=True)

for x in test.query('holiday==1').index:
    ax.axvline(x=x,color='k',alpha=0.8);
    
from statsmodels.tools.eval_measures import mse, rmse

rmse(test['total'],predictions)

fcast = result.predict(start,end+50,exog=test[['holiday']]).rename('SARIMAX with Exogoneous')

fcast.plot(figsize=(12,7),legend=True)




   


