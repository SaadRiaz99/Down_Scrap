import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import io
import os

# 1. Data Collection
print("Collecting data...")
url = "https://raw.githubusercontent.com/sharmaroshan/Online-Shoppers-Purchasing-Intention/master/online_shoppers_intention.csv"
response = requests.get(url)
df = pd.read_csv(io.StringIO(response.text))

# Save local copy
df.to_csv("human_behavior_data.csv", index=False)
print(f"Dataset saved to human_behavior_data.csv. Shape: {df.shape}")

# 2. Analysis & Visualization
plt.figure(figsize=(15, 12))

# Subplot 1: Data Size (Rows vs Columns)
plt.subplot(2, 2, 1)
size_data = {'Rows': df.shape[0], 'Columns': df.shape[1]}
plt.bar(size_data.keys(), size_data.values(), color=['skyblue', 'salmon'])
plt.title('Data Size (Rows & Columns)')
for i, v in enumerate(size_data.values()):
    plt.text(i, v + 0.1, str(v), ha='center')

# Subplot 2: Missing Values per Feature
plt.subplot(2, 2, 2)
missing_values = df.isnull().sum()
missing_values.plot(kind='bar', color='orange')
plt.title('Missing Values per Feature')
plt.xticks(rotation=45, ha='right')

# Subplot 3: Correlation Heatmap (Numeric features only)
plt.subplot(2, 2, 3)
numeric_df = df.select_dtypes(include=['float64', 'int64', 'bool'])
corr = numeric_df.corr()
sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Matrix')

# Subplot 4: Target Variable Distribution (Revenue)
plt.subplot(2, 2, 4)
sns.countplot(x='Revenue', data=df, palette='viridis')
plt.title('Behavior Outcome Distribution (Revenue)')

plt.tight_layout()
plt.savefig('behavior_analysis.png')
print("Analysis complete. Visualization saved as 'behavior_analysis.png'.")

# Print Summary for user
print("\n--- DATA SUMMARY ---")
print(f"Features: {list(df.columns)}")
print(f"Input Features Count: {len(df.columns) - 1}")
print(f"Output Feature: Revenue")
print(f"Total Entries: {len(df)}")
print("Missing Values Summary:")
print(df.isnull().sum()[df.isnull().sum() > 0] if df.isnull().sum().any() else "No missing values.")
