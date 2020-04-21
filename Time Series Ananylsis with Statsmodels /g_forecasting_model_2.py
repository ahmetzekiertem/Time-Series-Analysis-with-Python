#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:24:06 2020

@author: mac
"""


import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams



df = pd. read_csv('airline_passengers.csv',index_col='Month' ,parse_dates=True)



df.info()

'''
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 144 entries, 1949-01-01 to 1960-12-01
Freq: MS
Data columns (total 1 columns):
Thousands of Passengers    144 non-null int64
dtypes: int64(1)
memory usage: 2.2 KB
'''

df.index.freq = 'MS'

training_data = df.iloc[:109]

test_data = df.iloc[108:]


from statsmodels.tsa.holtwinters import ExponentialSmoothing

fitted_model = ExponentialSmoothing(training_data['Thousands of Passengers'],trend = 'mul',seasonal = 'mul',seasonal_periods=12).fit()

test_predictions = fitted_model.forecast(36)



training_data['Thousands of Passengers'].plot(legend=True,label='TRAIN',figsize = (12,5))
test_data['Thousands of Passengers'].plot(legend=True,label='TEST',figsize = (12,5))
test_predictions.plot(legend=True,label='PREDICTION',figsize=(12,5))


from sklearn.metrics import mean_squared_error, mean_absolute_error

mean_absolute_error(test_data, test_predictions)
#46.30290452191762

mean_squared_error(test_data, test_predictions)
#3075.328461982647

test_data.describe()
'''
       Thousands of Passengers
count                36.000000
mean                428.500000
std                  79.329152
min                 310.000000
25%                 362.000000
50%                 412.000000
75%                 472.000000
max                 622.000000
'''

np.sqrt(mean_squared_error(test_data, test_predictions))

# 55.45564409492191

final_model = ExponentialSmoothing(training_data['Thousands of Passengers'],trend = 'mul',seasonal = 'mul',seasonal_periods=12).fit()



df2 = pd. read_csv('samples.csv',index_col=0 ,parse_dates=True)



df2.info()


from statsmodels.tsa.statespace.tools import diff

diff(df2['b'], k_diff=1)
'''
Out[818]: 
1950-02-01    -5.0
1950-03-01    -5.0
1950-04-01    -2.0
1950-05-01    -2.0
1950-06-01     3.0
1950-07-01     8.0
1950-08-01    -8.0
1950-09-01     9.0
1950-10-01     2.0
1950-11-01    -1.0
1950-12-01    -4.0
1951-01-01     1.0
1951-02-01    -3.0
1951-03-01    -1.0
1951-04-01    14.0
1951-05-01   -12.0
1951-06-01     3.0
1951-07-01     3.0
1951-08-01    -8.0
1951-09-01    21.0
1951-10-01    -6.0
1951-11-01     2.0
1951-12-01   -10.0
1952-01-01     5.0
1952-02-01     0.0
1952-03-01    10.0
1952-04-01    -1.0
1952-05-01     3.0
1952-06-01     0.0
1952-07-01    -8.0

1957-07-01    11.0
1957-08-01   -12.0
1957-09-01    19.0
1957-10-01    -2.0
1957-11-01   -15.0
1957-12-01     5.0
1958-01-01     8.0
1958-02-01     0.0
1958-03-01    -9.0
1958-04-01    -2.0
1958-05-01    10.0
1958-06-01     0.0
1958-07-01    -9.0
1958-08-01     8.0
1958-09-01     3.0
1958-10-01   -10.0
1958-11-01    12.0
1958-12-01    -9.0
1959-01-01    10.0
1959-02-01     3.0
1959-03-01   -14.0
1959-04-01    19.0
1959-05-01   -10.0
1959-06-01     0.0
1959-07-01    -4.0
1959-08-01     3.0
1959-09-01     4.0
1959-10-01    -7.0
1959-11-01    17.0
1959-12-01   -14.0
Name: b, Length: 119, dtype: float64
'''


diff(df2['b'], k_diff=1).plot()





