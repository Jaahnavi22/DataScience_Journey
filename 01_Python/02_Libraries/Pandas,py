import pandas as pd

# Create Series
s = pd.Series([10, 20, 30, 40])
print(s)

# Create DataFrame
data = {
    "Name": ["A", "B", "C"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)

# View data
print(df.head())
print(df.tail())

# DataFrame information
print(df.shape)       # Rows and columns
print(df.columns)     # Column names
print(df.info())

# Select column
print(df["Name"])

# Select rows
print(df.iloc[0])     # First row
print(df.iloc[0:2])   # First two rows

# Add column
df["Result"] = ["Pass", "Pass", "Pass"]
print(df)

# Basic statistics
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())

# Filter data
print(df[df["Marks"] > 85])
