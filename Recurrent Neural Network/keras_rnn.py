#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 00:22:15 2020

@author: mac
"""

import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('Alcohol_Sales.csv',index_col ='DATE' ,parse_dates=True)

df.index.freq = 'MS'

df.columns = ['Sales']

from statsmodels.tsa.seasonal import seasonal_decompose

results = seasonal_decompose(df['Sales'])


train = df.iloc[:313]

test = df.iloc[313:]


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(train)

scaled_train = scaler.transform(train)
scaled_test = scaler.transform(test)


#[t1,t2,t3] --> [t4]

from keras.preprocessing.sequence import TimeseriesGenerator

n_input = 3

n_features = 1

generator = TimeseriesGenerator(scaled_train,scaled_train,length=n_input, batch_size =2)

 
len(scaled_train)

len(generator)

generator[0]

# (array([[[0.03658432],[0.03649885]]]), array([[0.08299855]]))
X,y = generator[0]

X.shape
#Out[229]: (1, 3, 1)

from keras.models import Sequential

from keras.layers import Dense 

from keras.layers import LSTM


n_input = 12

n_features = 1 #How many columns you have


train_generator = TimeseriesGenerator(scaled_train,scaled_train,length=n_input, batch_size =2)



model = Sequential()

model.add(LSTM(150,activation='relu', input_shape=(n_input, n_features)))

model.add(Dense(1))

model.compile(optimizer = 'adam', loss = 'mse')

model.summary()

model.fit_generator(train_generator, epochs=25)

model.history.history.keys()
myloss = model.history.history['loss']

plt.plot(range(len(model.history.history['loss'])),model.history.history['loss'])


#  12 history steps ------> step 13


first_eval_batch = scaled_train[-12:]

first_eval_batch =  first_eval_batch.reshape((1,n_input,n_features))

model.predict(first_eval_batch)



#FORECAST USING RNN 

test_predictions = [] #holding my predictions 
#last n_inputs points from the training set
first_eval_batch = scaled_train[-n_input:]
#reshape this to the format RNN wants(same format as TimeseriesGenerator)
current_batch = first_eval_batch.reshape((1,n_input,n_features))


#How far into the future will I forecast?
#len(test) ----> 24  

for i in range(len(test)):
    
    # One timestep ahead of historical 12 points 
    
    current_pred = model.predict(current_batch)[0]
    
    #store that predictions 
    
    test_predictions.append(current_pred)
    
    # UPDATE current_batch to include predictions
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis =1)



true_predictions = scaler.inverse_transform(test_predictions)

test['Predictions'] = true_predictions




