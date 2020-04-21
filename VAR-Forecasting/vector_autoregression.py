#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:29:31 2020

@author: mac
"""

import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose

import numpy as np

import warnings

warnings.filterwarnings("ignore")

from statsmodels.tsa.statespace.sarimax import SARIMAX

from statsmodels.tsa.stattools import adfuller

from statsmodels.tsa.api import VAR

from statsmodels.tools.eval_measures import rmse



from pmdarima import auto_arima

df1 = pd.read_csv('M2SLMoneyStock.csv',index_col =0 ,parse_dates=True)

df1.index.freq = 'MS'

df2 = pd.read_csv('PCEPersonalSpending.csv',index_col =0,parse_dates=True)

df2.index.freq = 'MS'

df1 = df1.join(df2)

df1 = df1.dropna()


def adf_test(series,title=''):
    """ 
    Pass in a time series and an optimal title, returns an ADF report
    
    """
    print(f'Augmented Dicky-Fuller Test:{title}')
    result = adfuller(series.dropna(), autolag='AIC') #dropna() handles differenced data
    
    labels = ['ADF test statistics','p-value','# lags used','# observations']
    
    out = pd.Series(result[0:4],index=labels)
    
    for key, value in result[4].items():
        
        out[f'critical value ({key})'] = value 
        
    print(out.to_string())
    
    if result[1] <= 0.05 :
        print("Strong evidence against the null hypothesis")
        print("Rehect the null ypothesis")
        print("Data has no unit root and is stationart")
        
    else :
        print("Weak evidence agaist the null hypothesis")
        print("Fail to reject the null hypothesis")
        print("Data has a unit root and  is non-stationart")
        

adf_test(df1['Money'])

adf_test(df1['Spending'])


df_transformed = df1.diff()

adf_test(df_transformed['Money'])

df_transformed = df_transformed.diff().dropna()


nobs = 12

train = df_transformed[:-nobs] #start = beginning of DF -12 FROM THE END


test = df_transformed[-nobs:] #START -12 FROM THE END OF DF GO TO END 



#GRIDSEARCH FOR ORDER p AR OF VAR model

model = VAR(train)


for p in [1,2,3,4,5,6,7]:
    results = model.fit(p)
    
    print(f'Order {p}')
    print(f'AIC: {results.aic}')
    print('\n')
    
    
results = model.fit(5)

results.summary()



# Grap 5 lagged values, right before the test starts!

#Numpy array

lagged_values =  train.values[-5:]

z = results.forecast(y=lagged_values, steps=12)


idx = pd.date_range('2015-01-01', periods=12,freq='MS')



df_forecast = pd.DataFrame(data=z,index=idx, columns=['Money_2d','Spending_2d'])

df_forecast['Money1d'] = (df1['Money'].iloc[-nobs-1]-df1['Money'].iloc[-nobs-2])+df_forecast['Money_2d']

df_forecast['MoneyForecast'] = df1['Money'].iloc[-nobs-1]+ df_forecast['Money1d'].cumsum()



df_forecast['Spending1d'] = (df1['Spending'].iloc[-nobs-1]-df1['Spending'].iloc[-nobs-2])+df_forecast['Spending_2d']


df_forecast['SpendingForecast'] = df1['Spending'].iloc[-nobs-1]+ df_forecast['Spending1d'].cumsum()

test_range = df1[-nobs:]

df_forecast[['SpendingForecast','MoneyForecast']].plot(legend=True)

test_range['Money'].plot(legend=True)

test_range['Spending'].plot(legend=True)

rmse(test_range['Money'],df_forecast['MoneyForecast'])

df_forecast['MoneyForecast'].mean()








