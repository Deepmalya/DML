# Script: LREGR1.PY
# Author: Debdulal Mandal
# Purpose: Demonstration of Linear regression using X, Y values
# Date of update: 25-Dec-2019
import numpy as np
from sklearn import linear_model

train_ArX = np.array([1,2,3,4])
train_ArY = np.array([5,8,11,14])

print("Training data X:")
print(train_ArX)
print("Training data Y:")
print(train_ArY)

train_ArX2D = np.zeros((4,2))
train_ArX2D[:,0] = train_ArX

regr = linear_model.LinearRegression()
regr.fit(train_ArX2D, train_ArY)
print("Estimated intercept:", regr.intercept_)
print("Estimated coefficients:", regr.coef_)
# Predict Y based on test values of X
test_ArX = np.array([2.5, 5])
test_ArX2D = np.zeros((2,2))
test_ArX2D[:,0] = test_ArX 
test_Y = regr.predict(test_ArX2D)
print("Test values of X:",test_ArX)
print("Predicted values of Y: ", test_Y)