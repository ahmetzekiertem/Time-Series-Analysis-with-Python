#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:53:27 2020

@author: mac
"""

import pandas as pd

pop = pd.read_csv("/Users/mac/Desktop/Udemy Time Series Analysies/Data/population_by_county.csv")

pop.head()

pop['State'].count()

pop['State'].nunique()

pop['State'].unique()
 
'''
 array(['South Carolina', 'Louisiana', 'Virginia', 'Idaho', 'Iowa',
       'Kentucky', 'Missouri', 'Oklahoma', 'Colorado', 'Illinois',
       'Indiana', 'Mississippi', 'Nebraska', 'North Dakota', 'Ohio',
       'Pennsylvania', 'Washington', 'Wisconsin', 'Vermont', 'Minnesota',
       'Florida', 'North Carolina', 'California', 'New York', 'Wyoming',
       'Michigan', 'Alaska', 'Maryland', 'Kansas', 'Tennessee', 'Texas',
       'Maine', 'Arizona', 'Georgia', 'Arkansas', 'New Jersey',
       'South Dakota', 'Alabama', 'Oregon', 'West Virginia',
       'Massachusetts', 'Utah', 'Montana', 'New Hampshire', 'New Mexico',
       'Rhode Island', 'Nevada', 'District of Columbia', 'Connecticut',
       'Hawaii', 'Delaware'], dtype=object)
'''

pop['County'].value_counts().head()


pop.sort_values('2010Census')

pop.sort_values('2010Census',ascending=False).head()

pop.groupby('State').sum()['2010Census']

pop.groupby('State').sum().sort_values('2010Census')

pop[pop['2010Census']>1000000]

len(pop[pop['2010Census']>1000000])
#39

def check_county(name):
    return "County" not in name 

pop['County'].apply(check_county)

myser = pop['County'].apply(lambda name : "County" not in name)

sum(pop['County'].apply(lambda name : "County" not in name))

states = pop.groupby('State').sum()

states['PercentChange'] = 100*(states['2017PopEstimate']-states['2010Census'])/states['2010Census']


states.sort_values('PercentChange',ascending=False).head()


'''
                      2010Census  2017PopEstimate  PercentChange
State                                                           
District of Columbia      601723           693972      15.330808
Texas                   25145561         28304596      12.562993
North Dakota              672591           755393      12.310899
Utah                     2763885          3101833      12.227282
Florida                 18801310         20984400      11.611372
'''













states.sort_values('PercentChange')