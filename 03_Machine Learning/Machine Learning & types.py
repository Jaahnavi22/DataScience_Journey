# INTRODUCTION TO MACHINE LEARNING
# ML is a subset of AI that learns patterns from data
# and makes predictions without explicit programming.

# TYPES OF MACHINE LEARNING

# 1. SUPERVISED LEARNING
# Learns from labelled data.

from sklearn.linear_model import LinearRegression

model = LinearRegression()

X = [[1], [2], [3], [4]]
y = [10, 20, 30, 40]

model.fit(X, y)                    # Trains the model
print(model.predict([[5]]))        # Predicts output


# 2. UNSUPERVISED LEARNING
# Finds patterns in unlabelled data.

from sklearn.cluster import KMeans

data = [[10], [12], [50], [52]]

model = KMeans(n_clusters=2, random_state=42, n_init=10)
model.fit(data)

print(model.labels_)               # Displays clusters


# 3. REINFORCEMENT LEARNING
# Learns through rewards and penalties.
# Example: A robot learns to reach a destination
# by receiving rewards for correct actions.
