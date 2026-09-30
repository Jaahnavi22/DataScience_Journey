# SAMPLING
# Sampling is the process of selecting a smaller group
# from a large population for analysis.

import random

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1. SIMPLE RANDOM SAMPLING
# Every item has an equal chance of being selected.

sample = random.sample(data, 3)
print(sample)


# 2. SYSTEMATIC SAMPLING
# Selects items at a fixed interval.

sample = data[::2]
print(sample)


# 3. STRATIFIED SAMPLING
# Divides population into groups and selects from each group.

group1 = [1, 2, 3, 4, 5]
group2 = [6, 7, 8, 9, 10]

sample = [random.choice(group1), random.choice(group2)]
print(sample)


# 4. CLUSTER SAMPLING
# Divides population into groups and selects entire groups.

cluster = [group1, group2]
sample = random.choice(cluster)

print(sample)
