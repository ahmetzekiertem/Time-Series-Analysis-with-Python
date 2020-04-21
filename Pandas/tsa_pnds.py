#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:45:37 2020

@author: mac
"""

import numpy as np
import pandas as pd 
from numpy.random import randn



labels = ['a','b','c']

mylist = [1,2,3 ]


arr = np.array(mylist)


d = {'a':11,'b':22,'c':33}


pd.Series(data=mylist)


pd.Series(data=arr,index=labels)



ser1 = pd.Series([10,22,33,44],index=['USA','Germany','England','Wales'])


ser2 = pd.Series([10,22,33,44],index=['USA','Germany','England','Italy'])

ser1+ser2
 

np.random.seed(100)

randa_mat = randn(5,4)

df= pd.DataFrame(data=randa_mat, index='A B C D E'.split(), columns='W X Y Z'.split())

mylist = ['W', 'X']

df[mylist]


df["NEW"]= df["W"]+df["X"]


df.drop('NEW', axis=1, inplace=True)

print(df)

df.loc[['A','B']][['X','Y']]
df.iloc[[O,3]]


df.drop('C',inplace=True)

df.loc['A']

    
