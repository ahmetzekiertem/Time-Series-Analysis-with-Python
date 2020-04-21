#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:14:29 2020

@author: mac
"""

import numpy as np
import pandas as pd
import matplotlib

from statsmodels.tsa.filters.hp_filter import hpfilter


df=pd.read_csv('macrodata.csv',index_col=0)


df.head()

gdp_cycle, gdp_trend = hpfilter(df['realgdp'],lamb=1600) 

type(gdp_trend) # pandas.core.series.Series


gdp_trend.plot()

df['trend'] = gdp_trend

df[['trend','realgdp']]['2005-01-01':].plot()
 