# UNSUPERVISED LEARNING
# Learns patterns from unlabelled data.
# Main tasks: Clustering and Dimensionality Reduction.

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.decomposition import PCA

data = [[10, 20], [12, 22], [50, 60], [52, 62], [11, 21]]

# 1. K-MEANS CLUSTERING
# Divides data into a fixed number of clusters.
model = KMeans(n_clusters=2, random_state=42, n_init=10)
print(model.fit_predict(data))

# 2. HIERARCHICAL CLUSTERING
# Creates clusters in a tree-like structure.
model = AgglomerativeClustering(n_clusters=2)
print(model.fit_predict(data))

# 3. DBSCAN
# Groups nearby data points and identifies noise.
model = DBSCAN(eps=5, min_samples=2)
print(model.fit_predict(data))

# 4. PCA
# Reduces the number of features while retaining
# as much information (variance) as possible.
model = PCA(n_components=1)
print(model.fit_transform(data))
