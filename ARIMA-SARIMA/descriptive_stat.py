#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:07:21 2020

@author: mac
"""

#test for stationarry
#tesf for independcetiy
#Augmented Dickey-Fuller test
 

import pandas as pd
import numpy as np

import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams

import statsmodels.api as sm
from statsmodels.tsa.stattools import acovf, acf, pacf, pacf_yw, pacf_ols 


#NON-STATIONARY

df1 = pd.read_csv('airline_passengers.csv', index_col = 'Month', parse_dates= True)


df1.index.freq = 'MS' 

#Stationary

df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col = 'Date',parse_dates= True )


df2.index.freq = 'D'

from statsmodels.tsa.stattools import adfuller

adfuller(df1['Thousands of Passengers'])
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



dftest = adfuller(df1['Thousands of Passengers'])

from statsmodels.tools.eval_measures import mse, rmse, meanabs

mse(df['test'],df['predictions']) #: 17.02

df4 = pd.read_csv('airline_passengers.csv', index_col = 'Month',parse_dates= True )

df4.index.freq = 'MS' 

from statsmodels.graphics.tsaplots import month_plot, quarter_plot

month_plot(df4['Thousands of Passengers']);


dfq = df4['Thousands of Passengers'].resample(rule = 'Q').mean()

quarter_plot(dfq)






 

dfout = pd.Series(dftest[0:4], index =['ADF Test Statisctics','p-value','#lags used','# Observations'] )
                  
                  
for key, val in dftest[4].items():
    dfout[f'critical value ({key})'] = val

dftest1 = adfuller(df2['Births'])  

dfout1 = pd.Series(dftest1[0:4], index =['ADF Test Statisctics','p-value','#lags used','# Observations'] )

    

df3 = pd.read_csv('samples.csv', index_col = 0, parse_dates= True)
    
df3.index.freq = 'MS' 

from statsmodels.tsa.stattools import grangercausalitytests

grangercausalitytests(df3[['a','d']], maxlag=3)

grangercausalitytests(df3[['b','d']], maxlag=3)

np.random.seed(42)

df = pd.DataFrame(np.random.randint(20,30,(50,2)),columns = ['test','predictions']);
    


    
    
                                      