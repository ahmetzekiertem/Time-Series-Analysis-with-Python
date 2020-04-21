#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:38:18 2020

@author: mac
"""

import numpy as np
import pandas as pd
df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
'''
df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0
'''

df.groupby(['Animal']).mean()
'''
        Max Speed
Animal
Falcon      375.0
Parrot       25.0
'''


df1 = pd.DataFrame({'col1':[1,2,2,4], 'col2':[333,444,555,666],'col3':['aaa','bbb','ccc','ddd']})

df1['col2'].unique() #show unrepeated values


df1['col1'].nunique() # number of uninique


df1['col1'].value_counts()

newdf = df1[(df1['col1']==2) & (df1['col2']== 444)]

def times_two(number):
    return number*2

df1['new'] = df1['col1'].apply(times_two)

df1.sort_values(by='col2',ascending=False)

df1.to_csv('newvie.csv')



    
