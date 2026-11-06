# SUPERVISED LEARNING
# Learns from labelled data (input + correct output).
# Types: Regression and Classification.

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

# Sample data
X = [[1], [2], [3], [4], [5], [6]]
y = [10, 20, 30, 40, 50, 60]

# 1. Linear Regression - Predicts continuous values
model = LinearRegression()
model.fit(X, y)
print(model.predict([[7]]))

# Classification data
X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

# 2. Logistic Regression - Predicts categories
model = LogisticRegression()
model.fit(X, y)
print(model.predict([[5]]))

# 3. Decision Tree - Uses decision rules
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)
print(model.predict([[5]]))

# 4. KNN - Uses nearest data points
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
print(model.predict([[5]]))

# 5. SVM - Finds the best separating boundary
model = SVC()
model.fit(X, y)
print(model.predict([[5]]))

# 6. Naive Bayes - Uses probability
model = GaussianNB()
model.fit(X, y)
print(model.predict([[5]]))

# 7. Random Forest - Combines multiple decision trees
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
print(model.predict([[5]]))
