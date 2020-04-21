#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:27:03 2020

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

df1 = pd.read_csv('airline_passengers.csv', index_col = 'Month', parse_dates= True)


df1.index.freq = 'MS' 

#Stationary

df2 = pd.read_csv('DailyTotalFemaleBirths.csv', index_col = 'Date',parse_dates= True )


df2.index.freq = 'D'

from statsmodels.tsa.stattools import adfuller

from pmdarima.arima import auto_arima

import warnings

warnings.filterwarnings('ignore')

help(auto_arima)



step_wise_fit = auto_arima(df2['Births'], start_p=0, start_q=0, max_p=6, max_q=3, seasonal=False, trace=True) 

step_wise_fit.summary()

step_wise_fit2 = auto_arima(df1['Thousands of Passengers'],  start_p=0, start_q=0, max_p=4, max_q=4, seasonal=True, trace=True, m =12)


