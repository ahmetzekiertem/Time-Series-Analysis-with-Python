#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:14:31 2020

@author: mac
"""


import pandas as pd
import numpy as np

import matplotlib 


df3 = pd.read_csv('df3.csv')

df3.plot.scatter(x='produced',y='defective',c='red',figsize=(12,3))

df3['produced'].plot.hist(edgecolor='k').autoscale(axis='x',tight=True)


df3[['weekday','produced']].boxplot(by='weekday',figsize=(12,10));

df3['defective'].plot.kde(ls='--')

df3.loc[0:30].plot.area(stacked=False,alpha=0.4)