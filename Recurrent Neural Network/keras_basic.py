#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:56:23 2020

@author: mac
"""

import keras
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

''' USING TENSERFLOW BACKEND ''' 


# y = mx + b + noise

m = 2 
b = 3 

x = np.linspace(0,50,100)


np.random.seed(101)

noise = np.random.normal(loc=0,scale=4,size=len(x))


y = 2*x + 3 + noise 


plt.plot(x,y,'*')

from keras.models import Sequential

from keras.layers import Dense 


model = Sequential()
model.add(Dense(4,input_dim=1,activation='relu'))

model.add(Dense(4, activation = 'relu'))

model.add(Dense(1, activation = 'linear'))

model.compile(loss='mse', optimizer = 'adam')

model.summary()

model.fit(x,y,epochs=200)

loss = model.history.history['loss']

epochs = range(len(loss))

plt.plot(epochs,loss)


x_for_predictions =np.linspace(0,50,100)

y_predicted = model.predict(x_for_predictions)

plt.plot(x,y,'*')
plt.plot(x_for_predictions, y_predicted,'r')

