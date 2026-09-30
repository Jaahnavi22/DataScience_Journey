import numpy as np
from scipy import stats

data = [10, 20, 20, 30, 40]

# Central tendency
print(np.mean(data))       # Mean
print(np.median(data))     # Median
print(stats.mode(data))    # Mode

# Dispersion
print(np.var(data))        # Variance
print(np.std(data))        # Standard deviation
print(max(data) - min(data))  # Range

# Position
print(np.percentile(data, 50))  # 50th percentile
print(np.percentile(data, 75))  # 75th percentile
