#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:38:07 2020

@author: mac
"""


import pandas as pd
import numpy as np

import matplotlib 

df1 = pd.read_csv('df1.csv',index_col=0)

ax = df1['C'].plot.line(figsize=(10,3),ls='--',c='red',lw=5)

title = 'my plot'
xlabel='x data'
ylabel = 'y data'

ax.set(xlabel=xlabel,ylabel=ylabel)

ax1=df1.plot()

ax1.legend(loc=6, bbox_to_anchor=(1.0,1.0))

