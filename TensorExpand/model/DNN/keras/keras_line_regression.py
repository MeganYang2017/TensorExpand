#! /usr/bin/python
# -*- coding: utf8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


X,Y=datasets.make_regression(200,1,n_targets=1,noise=10)

# plt.scatter(X,Y)
# plt.show()
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.3)

import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense

model=Sequential()
model.add(Dense(units=1,input_dim=1))
model.compile(loss='mse',optimizer='sgd')

# training
print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print('train cost: ', cost)

# test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

# plotting the prediction
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()
