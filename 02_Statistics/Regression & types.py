from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 1. LINEAR REGRESSION
# Predicts values using a straight-line relationship.

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([10, 20, 30, 40, 50])

model = LinearRegression()
model.fit(x, y)
print("Linear:", model.predict([[6]]))


# 2. POLYNOMIAL REGRESSION
# Captures curved relationships between variables.

poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
print("Polynomial:", model.predict(poly.transform([[6]])))
