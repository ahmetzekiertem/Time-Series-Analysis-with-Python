#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:31:21 2020

@author: mac
"""
import pandas as pd


from matplotlib import dates


df = pd.read_csv("UMTMVS.csv", parse_dates=True)


df.plot(figsize=(14,8))


df = df.set_index('DATE')
df.index = pd.to_datetime(df.index)



(df.loc['2019-01-01']-df.loc['2009-01-01'])/df.loc['2009-01-01']




100*(df.loc['2009-01-01']-df.loc['2008-01-01'])/df.loc['2008-01-01'] #how many increase there are between 2008-2009



df.loc['2005-01-01':].idxmin() # en dusuk ayi verir


#UMTMVS    2009-01-01
#dtype: object


df.sort_values(by='UMTMVS',ascending=False).head(5)
 

'''
              UMTMVS
DATE                
2018-08-01  529157.0
2018-10-01  527031.0
2018-06-01  525660.0
2018-03-01  518285.0
2018-09-01  516992.0
'''


df.loc['2008-01-01'] - df.loc['2009-01-01']

 

df['DATE'] = pd.to_datetime(df['DATE'])

df = df.set_index('DATE')




df.resample('Y').mean().plot.bar(figsize=(12,8))


yearly_date = df.resample('Y').mean()

yearly_data_shift = yearly_date.shift(1)

change = yearly_date - yearly_data_shift

change['UMTMVS'].idxmax()


df['Yearly Mean'] = df['UMTMVS'].rolling(window=12).mean()
df.plot(figsize=(14,8))

df2008 = df.loc['2008-01-01':'2009-01-01']


df2008.idxmax()

df_post_peak = df.loc['2008-01-01':]

df_post_peak[df_post_peak>=510081].dropna()


