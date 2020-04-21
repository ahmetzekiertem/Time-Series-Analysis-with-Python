#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:29:52 2020

@author: mac
"""

import pandas as pd
import numpy as np

import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams

import statsmodels.api as sm
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols 

from statsmodels.tsa.ar_model import AR, ARResults


df1 = pd.read_csv('uspopulation.csv', index_col = 'DATE', parse_dates= True)

df1.index.freq = 'MS'

train = df1.iloc[:84]

test = df1.iloc[84:]

import warnings  

warnings.filterwarnings('ignore')  #to ignore the warnings which is unnecessary

model = AR(train['PopEst'])

AR1fit = model.fit(maxlag=1)

AR1fit.k_ar

AR1fit.params

start = len(train)

end = len(train) + len(test) -1

prediction1 = AR1fit.predict(start=start, end= end)

prediction1 = prediction1.rename('AR1 Prediction')

test.plot()
prediction1.plot()


AR2fit = model.fit(maxlag=2)
AR2fit.params

prediction2 = AR2fit.predict(start=start, end= end)

prediction2 = prediction2.rename('AR2 Prediction')

test.plot()
prediction2.plot()
prediction1.plot()

ARfit = model.fit(ic = 't-stat')
ARfit.params

prediction8 =ARfit.predict(start,end)
prediction8 = prediction8.rename('AR8 Predcition')


'''
const        82.309677
L1.PopEst     2.437997
L2.PopEst    -2.302100
L3.PopEst     1.565427
L4.PopEst    -1.431211
L5.PopEst     1.125022
L6.PopEst    -0.919494
L7.PopEst     0.963694
L8.PopEst    -0.439511
dtype: float64
'''
from sklearn.metrics  import mean_squared_error

labels = ['AR1','AR2','AR8']
preds = [prediction1,prediction2, prediction8]

for i in range(3):
    error = mean_squared_error(test['PopEst'],preds[i])
    print(f'{labels[i]} MSE was : {error}')
    
    
'''
AR1 MSE was : 17449.714237833407
AR2 MSE was : 2713.258683668394
AR8 MSE was : 186.97263605698208
'''
model = AR(df1['PopEst'])
ARfit = model.fit()

forecasted_values = ARfit.predict(start=len(df1), end = len(df1)+24).rename('Forecast')

df1['PopEst'].plot(figsize = (12,8),legend = True)
forecasted_values.plot(figsize = (12,8),legend = True)



