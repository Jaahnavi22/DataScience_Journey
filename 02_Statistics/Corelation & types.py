import numpy as np

# POSITIVE CORRELATION
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
print("Positive:", np.corrcoef(x, y)[0, 1])

# NEGATIVE CORRELATION
x = [1, 2, 3, 4, 5]
y = [50, 40, 30, 20, 10]
print("Negative:", np.corrcoef(x, y)[0, 1])

# ZERO CORRELATION (approximately)
x = [1, 2, 3, 4, 5]
y = [3, 1, 5, 2, 4]
print("Zero:", np.corrcoef(x, y)[0, 1])
