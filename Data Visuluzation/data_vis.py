#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:52:43 2020

@author: mac
"""

import pandas as pd
import numpy as np

import matplotlib 
 

df1 = pd.read_csv('df1.csv',index_col=0)


df2 = pd.read_csv('df2.csv',index_col=0)

df1['A'].plot.hist(edgecolor='k')


df1['A'].plot.hist(bins=80,edgecolor='k').autoscale(enable=True,axis='both',tight=True)

df2.plot.bar()

df2.plot.bar(stacked=True)

df2.plot.barh(stacked=True)

df2.plot.barh()

df2.plot.line(y=['a','d','c'], figsize=(10,4),lw=4) #lw highlight lines

df2.plot.area(stacked=False,alpha=0.4)


df1.plot.scatter(x='A',y='B', c='C')

df1.plot.scatter(x='A',y='B', c='D')

df1.plot.scatter(x='A',y='B', c='D',cmap='cool')

df1.plot.scatter(x='A',y='B', c='D',cmap='coolwarm')


df2.plot.box()

df2.boxplot()

df2.plot.kde()

df3 = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df3.plot.scatter(x='a',y='b')

df3.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')


