import sys
import numpy as np 
import pandas as pd
import matplotlib
import sklearn
from sklearn.linear_model import LinearRegression
model = LinearRegression()
weight= [[1] , [2], [3], [4], [5]]
prices = [30, 60, 90, 120, 150]
model.fit(weight, prices)
prediction =model.predict([[10]])
print("prediction for input  5 is:",prediction)

import matplotlib.pyplot as plt
plt.scatter(weight, prices, color='blue', label='Data Points')

# Regression line
line_x = weight
line_y = model.predict(line_x)
plt.plot(line_x, line_y, color='red', linewidth=2, label='Regression Line')

# Labels and title
plt.xlabel('weight')
plt.ylabel('prices')
plt.title('linear Regression line ')
plt.legend()

plt.show()


