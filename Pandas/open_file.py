#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:49:16 2020

@author: mac
"""


import numpy as np
import pandas as pd

df= pd.read_csv('example.csv')


df1=pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')


#df1.drop('Unnamed',axis=1)

dfx = pd.read_html("https://www.hl.co.uk/shares/shares-search-results/g/glaxosmithkline-plc-ordinary-25p")
#read_html onemliii

dfx[2]

'''
   Type Ex-div date Payment date  Amount
0  Q4  *  20/02/2020   09/04/2020  23.00p
1     Q3  14/11/2019   09/01/2020  19.00p
2     Q2  08/08/2019   10/10/2019  19.00p
3     Q1  16/05/2019   11/07/2019  19.00p
4     Q4  21/02/2019   11/04/2019  23.00p
'''

dfx[3]
'''
Financialyear end        ...         Total dividendpaid
0        31/12/2019        ...                     80.00p
1        31/12/2018        ...                     80.00p
2        31/12/2017        ...                     80.00p
3        31/12/2016        ...                     80.00p
4        31/12/2015        ...                    100.00p

[5 rows x 4 columns]
'''
dfx[1]
'''
                        0           1           2
0            Year ending:  31/12/2019  31/12/2018
1            Revenue (£m)    33754.00    30821.00
2  Profit before tax (£m)     6221.00     4800.00
3       Adjusted EPS (p):      123.90      119.40
4               P/E ratio       14.40       12.50
5                     PEG        3.60        1.80
6          EPS growth (%)        4.00        7.00
'''
