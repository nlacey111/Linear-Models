import numpy as np
import matplotlib.pyplot as plt

X = np.array( [[20, 0], 
               [60, 0],
               [80,20],
               [80,80],
               [80,140]])

x = np.array([40, 80, 120, 180, 240])
Y = np.array([57, 176, 223, 161, 99]).T

# a)
# Find the least squares solution for the coefficients of the model Y = bX1 + cX2.
# The solution is given by the formula: (X^T X)^-1 X^T Y

coefficients = np.linalg.inv(X.T @ X) @ X.T @ Y
print(coefficients)

def predict(x):
    if x < 20:
        return 0
    elif x < 100:
        return coefficients[0]*(x-20)
    else:
        return coefficients[0]*(80) + coefficients[1]*(x-100)

Y_pred = np.zeros(len(x))
for i in range(len(x)):
    Y_pred[i] = predict(x[i])

print(Y_pred)

# plot the data and the model
plt.scatter(x, Y, label='Data')
# plot piecewise linear model
plt.plot([0, 20, 100, 180, 240], [0, 0, 80*coefficients[0], 80*coefficients[0] + 80*coefficients[1], 80*coefficients[0] + 140*coefficients[1]], label='Model')
plt.legend()
plt.show()


epsilon = np.abs(Y - Y_pred)
print(epsilon)

# find S^2 
S2 = np.sum(epsilon**2) / (len(Y) - 2)
print(S2)




    

