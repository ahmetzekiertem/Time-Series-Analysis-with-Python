#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:22:03 2020

@author: mac
"""

#ets model stands for Error, Trend, seasonality 


import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams


airline = pd. read_csv('airline_passengers.csv',index_col='Month',parse_dates=True)

airline.dropna()


airline.plot()

result =seasonal_decompose(airline['Thousands of Passengers'],model='multiplicative')

resul_trend = result.trend

seasonality = result.seasonal
residual_component = result.resid

result.plot();
rcParams['figure.figsize' ] = 12,5





#<statsmodels.tsa.seasonal.DecomposeResult at 0x122903ef0>

