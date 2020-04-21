#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:24:05 2020

@author: mac
"""



import pandas as pd


from matplotlib import dates


dfx = pd.read_csv('monthly_milk_production.csv', parse_dates=True)

title = "Monthly milk production pounds per cows : Jan 62 - Dec 75"

dfx.dtypes
'''
Date          object
Production     int64
dtype: object
'''

dfx['Date'] = pd.to_datetime(dfx['Date'])

dfx = dfx.set_index('Date')

print(len(dfx))
print(dfx.head())




dfx.info()




dfx['Month'] = dfx.index.strftime('%B')


dfx.boxplot(by='Month',figsize=(12,5))


dfx.groupby(['Month']).mean()


'''
           Production
Month                
April      800.071429
August     747.500000
December   721.000000
February   689.285714
January    727.071429
July       788.071429
June       836.142857
March      783.500000
May        862.785714
November   682.571429
October    711.857143
September  706.642857
'''



 