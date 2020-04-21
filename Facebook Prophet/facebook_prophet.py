#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:18:04 2020

@author: mac
"""

import pandas as pd

import matplotlib.pylot as plt

from fbprophet import Prophet


df = pd.read_csv('BeerWineLiquor.csv')

df.columns = ['ds','y']

df['ds'] = pd.to_datetime(df['ds'])

m = Prophet()

m.fit(df)

#placeholder

future = m.make_future_dataframe(periods=24,freq='MS')


forecast = m.predict(future)

forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']].tail(12)

m.plot(forecast);


forecast.plot(x = 'ds', y = 'yhat', figsize = (12,6))

m.plot_components(forecast);

train = df.iloc[:576]

test = df.iloc[576:]

m = Prophet()

m.fit(train)

future =  m.make_future_dataframe(periods = 12, freq = 'MS')

forecast = m.predict(future)


ax = forecast.plot(x = 'ds',y = 'yhat', label = 'Predictions', legend = True, figsize = (12,6))

test.plot(x='ds',y ='y',label= 'True Test Data', legend =True, ax = ax, xlim = ('2018-01-01','2019-01-01'))


from statsmodels.tools.eval_measures import rmse 

predictions = forecast.iloc[-12:]['yhat']


test['y']


rmse(predictions, test['y'])


test.mean()

from fbprophet.diagnostic import cross_validation, performance_metrics

from fbprophet.plot import plot_cross_validation_metrics



pd.Timedelta
#initial 

initial = 5*365

initial = str(initial) + 'days'


#period

period = 5 * 365
period = str(period) + ' days'

#horizon

horizon = 365
horizon = str(horizon) + ' days'


df_cv = cross_validation(m, initial = initial, period = period, horizon=horizon)


plot_cross_validation_metric(df_cv,metric = 'rmse')











