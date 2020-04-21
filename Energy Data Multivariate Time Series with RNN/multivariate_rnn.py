#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:46:40 2020

@author: mac
"""


import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('energydata_complete.csv',index_col ='date' ,parse_dates=True)



df = df.round(2)

df = df.loc['2016-05-01':]

from statsmodels.tsa.seasonal import seasonal_decompose

#how many rows there are in per day we know 10mins our frequencey 24*(60/10)=144

test_days = 2
test_ind = test_days*144


train = df.iloc[:-test_ind]

test = df.iloc[-test_ind:]


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(copy = True, feature_range = (0,1 ))

scaler.fit(train)

scaled_train = scaler.transform(train)
scaled_test = scaler.transform(test)


from keras.preprocessing.sequence import TimeseriesGenerator

n_input = 144

n_features = 1

generator = TimeseriesGenerator(scaled_train,scaled_train,length=n_input, batch_size =1)

X , y =generator[0]


from keras.models import Sequential

from keras.layers import Dense 

from keras.layers import LSTM

model = Sequential()

model.add(LSTM(150,activation='relu', input_shape=(n_input, scaled_train.shape[1])))

model.add(Dense(scaled_train.shape[1]))

model.compile(optimizer = 'adam', loss = 'mse')

model.summary()

from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=1)

validation_generator =TimeseriesGenerator(scaled_test, scaled_test, length = n_input, batch_size =1)

model.fit_generator(generator, epochs = 2, validation_data=validation_generator,callbacks=[early_stop])

first_eval_batch = scaled_train[-n_input:]


first_eval_batch = first_eval_batch.reshape((1,n_input,scaled_train.shape[1]))

model.predict(first_eval_batch)

n_features = scaled_train.shape[1]
test_predictions= []

first_eval_batch = scaled_train[-n_input:]

current_batch = first_eval_batch.reshape((1,n_input,28))

for i in range(len(test)):
    
    current_pred = model.predict(current_batch)[0]
    
    test_predictions.append(current_pred)
    
    current_batch = np.append(current_batch[:,1:,:], [[current_pred]], axis =1)
    

model.history.history.keys()

losses = pd.DataFrame(model.history.history)

losses.plot 
    
true_predictions = scaler.inverse_transform(test_predictions)

true_predictions = pd.DataFrame(data=true_predictions, columns=test.columns)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



