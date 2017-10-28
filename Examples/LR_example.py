# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:39:46 2017

@author: Khiati Zakaria
"""

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


x_data = []
y_data = []


file = open("dataset","r")

for line in file:
    x = line.split("\t")
    x_data.append(float(x[1]))
    y_data.append(float(x[2]))

x_train = np.array(x_data[:22500]).reshape(-1, 1)
y_train = np.array(y_data[:22500]).reshape(-1, 1)

x_test = np.array(x_data[22500:]).reshape(-1, 1)
y_test = np.array(y_data[22500:])

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
score = linear.score(x_test, y_test)



predicted= linear.predict(x_test)
result=predicted.reshape(1, -1)[0]

print('score : ', score)
print('Coefficient: ', linear.coef_[0][0])
print("Mean squared error: %.2f" % mean_squared_error(y_test, result))
print('Variance score: %.2f' % r2_score(y_test, result))

# Plot outputs
plt.scatter(x_test, y_test,  color='black')
plt.plot(x_test, result, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()