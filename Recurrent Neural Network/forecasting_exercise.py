#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:53:21 2020

@author: mac
"""

import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose

import numpy as np

import warnings

warnings.filterwarnings("ignore")

from statsmodels.tsa.statespace.sarimax import SARIMAX

from statsmodels.tsa.stattools import adfuller

from statsmodels.tsa.api import VAR

from statsmodels.tools.eval_measures import rmse

from statsmodels.tsa.statespace.varmax import VARMAX, VARMAXResults

import matplotlib


from statsmodels.tools.eval_measures import rmse



from pmdarima import auto_arima

from sklearn.metrics import mean_squared_error


df1 = pd.read_csv('HospitalityEmployees.csv',index_col ='Date' ,parse_dates=True)

df1.index.freq = 'MS'

df1['Employees'].plot(figsize=(12,5))

result = seasonal_decompose(df1['Employees'],model='add')

auto_arima(df1['Employees'], seasonal=True,m=12).summary()

nobs = 12

train = df1.iloc[:len(df1)-12] #start = beginning of DF -12 FROM THE END
test = df1.iloc[len(df1)-12:]


model = SARIMAX(train['Employees'],order=(1,1,2),seasonal_order=(1,0,1,12))
result = model.fit()
result.summary()

start = len(train)
end = len(test) + len(train) -1

predictions = result.predict(start,end,typ='levels').rename('SARIMA TEST pREDICTIONS')

test['Employees'].plot()
predictions.plot()

rmse(test['Employees'],predictions)

fcast = result.predict(start,end+16,typ='levels').rename('SARIMA forecasting')

df1['Employees'].plot(legend =True)
fcast.plot()



 

