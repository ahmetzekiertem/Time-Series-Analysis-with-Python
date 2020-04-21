#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:53:50 2020

@author: mac
"""

import pandas as pd
import numpy as np

import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams

import statsmodels.api as sm
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols 


#NON-STATIONARY

df1 = pd.read_csv('TradeInventories.csv', index_col = 'Date', parse_dates= True)


df1.index.freq = 'MS' 

#Stationary

df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col = 'Date',parse_dates= True )


df2.index.freq = 'D'

df2 = df2[:120]

from statsmodels.tsa.arima_model import ARMA, ARIMA, ARMAResults

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

from pmdarima import auto_arima # grid search library


#ARMA Model 

from statsmodels.tsa.stattools import adfuller

adfuller(df2['Births'])
'''
(0.8153688792060423,
 0.9918802434376409,
 13,
 130,
 {'1%': -3.4816817173418295,
  '5%': -2.8840418343195267,
  '10%': -2.578770059171598},
 996.6929308390189)
'''

help(adfuller)



dftest = adfuller(df2['Births'])

dfout = pd.Series(dftest[0:4], index =['ADF Test Statisctics','p-value','#lags used','# Observations'] )
                  
                  
for key, val in dftest[4].items():
    dfout[f'critical value ({key})'] = val


step_wise_fit = auto_arima(df2['Births'],seasonal=False).summary()

train = df2.iloc[:90]
test = df2.iloc[90:]

model = ARMA(train['Births'], order = (2,2))

results = model.fit()

start = len(train)

end = len(train) + len (test) - 1

predictions = results.predict(start, end).rename('ARMA (2,2) Predictions')
