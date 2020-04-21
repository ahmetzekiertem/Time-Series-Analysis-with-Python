#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:38:35 2020

@author: mac
"""

import pandas as pd
import numpy as np

from datetime import datetime

import matplotlib 

my_year = 2020
my_month = 1
my_day = 2
my_hour = 13
my_min = 50
my_sec= 33

my_date = datetime(my_year,my_month,my_day,my_hour,my_min,my_sec)

my_date.day

np.array(['2020-03-15','2020-03-16','2020-03-16'],dtype='datetime64')#defauld day precedure


np.array(['2020-03-15','2020-03-16','2020-03-16'],dtype='datetime64[Y]')

 

np.arange('2020-03-15','2020-06-30',7,dtype='datetime64')


np.arange('2001','2020',dtype='datetime64[Y]')


#PANDAS DATETIME
pd.date_range('2020-01-01',periods=7,freq='D')

pd.date_range('Jan 01, 2018',periods=40,freq='D')

pd.to_datetime(['1/2/2018','Jan 03, 2018'])

# DatetimeIndex(['2018-01-02', '2018-01-03'], dtype='datetime64[ns]', freq=None)

pd.to_datetime(['2--1--2018','3--4--2018'],format='%d--%m--%Y')


data = np.random.randn(6,3)

cols = ['A','B','C']

idx = pd.date_range('2020-01-01',periods=6,freq='D')

df=pd.DataFrame(data,index=idx,columns=cols)




