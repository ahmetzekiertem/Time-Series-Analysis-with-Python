#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:57:20 2020

@author: mac
"""

import numpy as np
import pandas as pd
 
df = pd.DataFrame({'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]})
 

df.dropna(axis=1) # as vertical value will be showed.

df.dropna(thres=2)# we did put a threshold to display NaN value.

df.fillna(value='FILL Value' ,inplace=True)

df.fillna(value=df.mean())

df['A'].fillna(value=df['A'].mean())