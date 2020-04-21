
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:37:17 2020

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

from statsmodels.tsa.statespace.varmax import VARMAX, VARMAXResults

import matplotlib


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


auto_arima(df1['Money'], maxiter=1000)


auto_arima(df1['Spending'], maxiter=1000)

df_transformed = df1.diff().diff()

df_transformed = df_transformed.dropna()

nobs = 12

train, test = df_transformed[0:-nobs], df_transformed[-nobs:]

model = VARMAX(train,order=(1,2), trend='c')

results = model.fit(maximer=1000,disp=False)

results.summary()

df_forecast = results.forecast(12)

df_forecast


df_forecast['Money1d'] = (df1['Money'].iloc[-nobs-1]-df1['Money'].iloc[-nobs-2])+df_forecast['Money']

df_forecast['MoneyForecast'] = df1['Money'].iloc[-nobs-1]+ df_forecast['Money1d'].cumsum()



df_forecast['Spending1d'] = (df1['Spending'].iloc[-nobs-1]-df1['Spending'].iloc[-nobs-2])+df_forecast['Spending']


df_forecast['SpendingForecast'] = df1['Spending'].iloc[-nobs-1]+ df_forecast['Spending1d'].cumsum()

df1['Money'][-nobs].plot().autoscale(axis='x',tight=True)

df_forecast['MoneyForecast'].plot()

df_forecast['SpendingForecast'].plot()





