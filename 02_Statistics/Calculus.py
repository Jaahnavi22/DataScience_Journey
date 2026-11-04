import sympy as sp

x = sp.symbols('x')

# Function
f = x**2 + 3*x

# Differentiation: Finds rate of change
print("Derivative:", sp.diff(f, x))

# Integration: Finds accumulated area
print("Integration:", sp.integrate(f, x))

# Limit: Finds approaching value
limit = (x**2 - 1) / (x - 1)
print("Limit:", sp.limit(limit, x, 1))
