#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:16:24 2020

@author: mac
"""

import numpy as np
import pandas as pd 
from numpy.random import randn


randas = randn(10,5)


df= pd.DataFrame(data=randas, index='A B C D E F G H J K'.split(), columns='W X Y Z M'.split())


df_boolean = df>1

df[df>1]


#df[df['W'] > 0]['X'].loc['H']#ILK COLUMN sonro row girildi.

cond1 = df['W']>-1
cond2 = df['Y']>0

df[(cond1) & (cond2)]


new_ind = 'UCW NY CA OR CO MY GE SA SK TE'.split()

df['States'] = new_ind

df.info()

'''
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, A to K
Data columns (total 6 columns):
W         10 non-null float64
X         10 non-null float64
Y         10 non-null float64
Z         10 non-null float64
M         10 non-null float64
States    10 non-null object
dtypes: float64(5), object(1)
memory usage: 560.0+ bytes
'''

df.describe()

'''
               W          X          Y          Z          M
count  10.000000  10.000000  10.000000  10.000000  10.000000
mean   -0.314554  -0.024369  -0.080655  -0.203410  -0.208197
std     0.850082   0.997665   1.256638   1.351978   1.001355
min    -1.797638  -1.681387  -2.023764  -2.141852  -1.364477
25%    -0.741605  -0.645898  -0.782750  -1.050297  -0.875149
50%    -0.315310   0.178477  -0.340244  -0.344667  -0.609970
75%     0.064506   0.593211   0.554259   0.496632   0.311898
max     1.197417   1.240190   2.549286   1.940623   1.524863
'''
df.set_index('States',inplace=True)

df['W'].loc['CO']

ser_w = df['W']>0


ser_w.value_counts()
'''
True     8
False    2
Name: W, dtype: int64
'''

 
 