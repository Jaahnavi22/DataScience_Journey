import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Line plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# Bar chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Histogram
marks = [50, 60, 65, 70, 70, 75, 80, 85, 90]
plt.hist(marks)
plt.title("Marks Distribution")
plt.show()

# Pie chart
values = [30, 20, 50]
labels = ["Python", "SQL", "ML"]

plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Skills")
plt.show()
