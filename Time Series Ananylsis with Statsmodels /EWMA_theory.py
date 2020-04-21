#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:00:50 2020

@author: mac
"""

'''
SMA Simple Moving Averages same exact window size 

Descriping more simple model

EWMA Exponential weighted moving averages:
    it would be better recent data be weighted more than
    older data.
    we do this by implementing a EWMA instead of SMA
    
    
Basic SMA has some 'weakness' 
    smaller windows will lead to more noises, rather than signal
    
    '''


import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams


airline = pd. read_csv('airline_passengers.csv',index_col='Month',parse_dates=True)


airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

airline['6-months-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()

airline['12-months-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()

airline.plot(figsize=(10,8))


airline['EWMA-12']= airline['Thousands of Passengers'].ewm(span=12).mean()

airline[['Thousands of Passengers','EWMA-12']].plot(figsize=(10,8))

