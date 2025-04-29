# housing_price_eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/housing.csv")  # Replace with correct path
print("Data loaded successfully.")

# Basic Info
print(df.head())
print(df.info())
print(df.describe())

# Checking for missing values
print("\nMissing values:\n", df.isnull().sum())

# Fill missing 'total_bedrooms' with median
df['total_bedrooms'].fillna(df['total_bedrooms'].median(), inplace=True)

# EDA - Visualizations
sns.histplot(df['median_house_value'], bins=50, kde=True)
plt.title("Distribution of Median House Value")
plt.xlabel("Median House Value")
plt.ylabel("Frequency")
plt.show()

sns.scatterplot(x='longitude', y='latitude', hue='median_house_value', data=df, palette='viridis', alpha=0.5)
plt.title("Geographical Distribution of House Prices")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Price vs other features
features = ['median_income', 'housing_median_age', 'total_rooms', 'population']
for feature in features:
    sns.scatterplot(data=df, x=feature, y='median_house_value', alpha=0.4)
    plt.title(f"{feature} vs Median House Value")
    plt.show()

# Feature Engineering
