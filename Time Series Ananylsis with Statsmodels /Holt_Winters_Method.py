#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:45:49 2020

@author: mac
"""

# triple exponentially smoothing  alfa beta(trend) gama(seasonality)


import numpy as np
import pandas as pd
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams

 
airline = pd. read_csv('airline_passengers.csv',index_col='Month',parse_dates=True)


airline.dropna(inplace=True)

airline.index = pd.to_datetime(airline.index)

airline.index.freq =  'MS'


from statsmodels.tsa.holtwinters import SimpleExpSmoothing
 
 
span=12
alpha = 2/(span+1)
 
airline['EWMA12'] = airline['Thousands of Passengers'].ewm(alpha=alpha,adjust=False).mean()

model = SimpleExpSmoothing(airline['Thousands of Passengers'])
 
fitted_model = model.fit(smoothing_level=alpha,optimized=False)


#Double Exponential Smoothing Method which includes trend info in model


 
from statsmodels.tsa.holtwinters import ExponentialSmoothing


#we can use mulitolicative or additive adjustment

airline['DSA_add_12'] = ExponentialSmoothing(airline['Thousands of Passengers'],trend='add').fit().fittedvalues.shift(-1) # code add represent additive model


#DSA IS MORE CLOSE TO THE OBSERVED GRAPH LINE dOUBLE eXPONENTIAL SMOOTHING


airline['DSA_mul_12'] = ExponentialSmoothing(airline['Thousands of Passengers'],trend='mul').fit().fittedvalues.shift(-1)

airline.iloc[:24].plot() # we can see how they are close with zoom.



#triple exponential smoothing 



airline['TES_mul_12'] = ExponentialSmoothing(airline['Thousands of Passengers'],trend='mul',seasonal='mul',seasonal_periods=12).fit().fittedvalues.shift(-1)





  



