#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:32:05 2020

@author: mac
"""

#Correlation means stresnght of two valuable each others. -1,+1

'''

Autocorralation is correlagram

shows the correlation of the series with itself,
lagged by x time units .
=== y axis is the correlation units x axis is the number of units of lag
'''

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

df1.head()
df2.head()

import warnings  

warnings.filterwarnings('ignore')  #to ignore the warnings which is unnecessary

df = pd.DataFrame({'a':[12,5,11,12,9]})

acf(df['a'])

pacf_yw(df['a'],nlags=4,method='mle')

pacf_yw(df['a'],nlags=4,method='unbiased')

pacf_ols(df['a'], nlags=4)

'''
Method in the above use different types of calculation corralation itself
'''

from pandas.plotting import lag_plot

lag_plot(df1['Thousands of Passengers'])

lag_plot(df2['Births'])

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(df1,lags=40)
plot_acf(df2,lags=40)

plot_pacf(df2,lags=40, title = 'Daily Birth Female')


