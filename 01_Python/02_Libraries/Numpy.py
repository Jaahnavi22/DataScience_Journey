import numpy as np

# Create NumPy array
a = np.array([1, 2, 3, 4, 5])
print(a)

# 2D array
b = np.array([[1, 2], [3, 4]])
print(b)

# Array properties
print(a.ndim)      # Number of dimensions
print(a.shape)     # Shape of array
print(a.size)      # Number of elements
print(a.dtype)     # Data type

# Create arrays
print(np.zeros(3))       # Array of zeros
print(np.ones(3))        # Array of ones
print(np.arange(1, 6))   # Range of values

# Mathematical operations
print(a + 2)
print(a * 2)

# Statistical functions
print(np.sum(a))         # Sum
print(np.mean(a))        # Mean
print(np.max(a))         # Maximum
print(np.min(a))         # Minimum

# Indexing and slicing
print(a[0])              # First element
print(a[1:4])            # Slicing
