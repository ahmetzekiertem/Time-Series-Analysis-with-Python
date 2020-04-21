#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:07:33 2020

@author: mac
"""

import pandas as pd

import matplotlib.pylot as plt

from fbprophet import Prophet


df = pd.read_csv('airline_passengers.csv')


df.columns = ['ds','y']

df['ds'] = pd.to_datetime(df['ds'])

m = Prophet()


m.fit(df)

future = m.make_future_dataframe(50,freq='MS')

forecast = m.predict(future)

fig = m.plot(forecast)

fig = m.plot_components(forecast);


from fbprophet.plot import add_changepoints_to_plot

fig = m.plot(forecast)

a = add_changepoints_to_plot(fig.gca(),m,forecast)

