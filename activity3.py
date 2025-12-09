import sys
import numpy as np 
import pandas as pd
import matplotlib
import sklearn


print("=== Library Versions ===")
print(f"Python:{sys.version.split()[0]}")
print(f"Numpy:{np.__version__}")
print(f"Pandas:{pd.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"sklearn:{sklearn.__version__}")


from sklearn.linear_model import LinearRegression
model = LinearRegression()
X = [[1] , [2], [3], [4]]
y = [2, 4, 6, 8]
model.fit(X, y)
prediction =model.predict([[10]])
print("prediction for input  5 is:",prediction)

import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Data Points')

# Regression line
line_x = X
line_y = model.predict(line_x)
plt.plot(line_x, line_y, color='red', linewidth=2, label='Regression Line')

# Labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('linear Regression line ')
plt.legend()

plt.show()


