import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# View data
print(df.head())

# Dataset information
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Statistical summary
print(df.describe())

# Check duplicate rows
print(df.duplicated().sum())

# Check unique values
print(df.nunique())

# Correlation
print(df.corr(numeric_only=True))

# Sort data
print(df.sort_values("Marks"))

# Filter data
print(df[df["Marks"] > 80])
