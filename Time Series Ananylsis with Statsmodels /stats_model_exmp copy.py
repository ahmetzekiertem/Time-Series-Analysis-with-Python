#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:03:46 2020

@author: mac
"""

import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams




df = pd. read_csv('EnergyProduction.csv',index_col=0,parse_dates=True)

df.index.freq = 'MS'





df['SMA12'] = df['EnergyIndex'].rolling(window=12).mean()

df.plot(figsize=(12,5))

from statsmodels.tsa.holtwinters import SimpleExpSmoothing


df['SES12'] = SimpleExpSmoothing(df['EnergyIndex']).fit(smoothing_level=2/(12+1),optimized=False).fittedvalues.shift(-1)

from statsmodels.tsa.holtwinters import ExponentialSmoothing

df['TESmul-12'] = ExponentialSmoothing(df['EnergyIndex'],trend = 'mul',seasonal='mul',seasonal_periods=12).fit().fittedvalues.shift(-1)


df[:'1972-01-01'].plot(figsize=(12,5))

