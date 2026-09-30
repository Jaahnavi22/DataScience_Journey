# CENTRAL LIMIT THEOREM (CLT)

import numpy as np

data = np.arange(1, 101)

# Take random samples and calculate their means
sample_means = []

for i in range(100):
    sample = np.random.choice(data, 10)
    sample_means.append(np.mean(sample))

print(np.mean(sample_means))
