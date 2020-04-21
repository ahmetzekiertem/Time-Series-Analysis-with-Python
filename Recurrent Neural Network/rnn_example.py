#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:03:48 2020

@author: mac
"""

import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('Miles_Traveled.csv',index_col ='DATE' ,parse_dates=True)

df.index.freq = 'MS'

df.columns = ['Value']

from statsmodels.tsa.seasonal import seasonal_decompose

results = seasonal_decompose(df['Value'])


train = df.iloc[:576]

test = df.iloc[576:]


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(copy = True, feature_range = (0,1 ))

scaler.fit(train)

scaled_train = scaler.transform(train)
scaled_test = scaler.transform(test)


from keras.preprocessing.sequence import TimeseriesGenerator

n_input = 24

n_features = 1

generator = TimeseriesGenerator(scaled_train,scaled_train,length=n_input, batch_size =1)

from keras.models import Sequential

from keras.layers import Dense 

from keras.layers import LSTM


model = Sequential()

model.add(LSTM(150,activation='relu', input_shape=(n_input, n_features)))

model.add(Dense(1))

model.compile(optimizer = 'adam', loss = 'mse')

model.summary()


#fit model to the generator (it should be a lot of epoches, but do as many as you have the patience for!)


model.model.fit_generator(generator, epochs=30)

loss_per_epochs = model.history.history['loss']

plt.plot(range(len(loss_per_epochs)),loss_per_epochs)

test_predictions = []

first_eval_batch = scaled_train[-n_input:]

current_batch = first_eval_batch.reshape((1,n_input,n_features))


for i in range(len(test)):
    
    current_pred = model.predict(current_batch)[0]
    
    test_predictions.append(current_pred)
    current_batch = np.append(current_batch[:,1:,:],[[current_pred]], axis =1)
    
true_predictions = scaler.inverse_transform(test_predictions)

test['Predictions'] = true_predictions


model.save('solutions.h5')
