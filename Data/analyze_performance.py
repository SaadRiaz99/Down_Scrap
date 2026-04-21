import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Create Synthetic Data (Mobile Usage vs Academic Performance)
np.random.seed(42)
n_samples = 1000

data = {
    'Student_ID': range(1, n_samples + 1),
    'Age': np.random.randint(18, 25, n_samples),
    'Gender': np.random.choice(['Male', 'Female'], n_samples),
    'Mobile_Usage_Hours': np.random.uniform(1, 10, n_samples), # 1 to 10 hours daily
    'Social_Media_Hours': np.random.uniform(0, 6, n_samples),
    'Study_Hours': np.random.uniform(1, 8, n_samples),
    'Sleep_Hours': np.random.uniform(4, 9, n_samples),
}

# Create a realistic 'Exam_Score' based on other features
# Increase Study/Sleep -> Increase Score
# Increase Mobile/Social Media -> Decrease Score
base_score = 50
score = (base_score 
         + (data['Study_Hours'] * 4) 
         + (data['Sleep_Hours'] * 2) 
         - (data['Mobile_Usage_Hours'] * 3) 
         - (data['Social_Media_Hours'] * 2) 
         + np.random.normal(0, 5, n_samples))

data['Exam_Score'] = np.clip(score, 0, 100)

df = pd.DataFrame(data)

# Introduce some missing values for the analysis part
df.loc[np.random.choice(df.index, 20), 'Sleep_Hours'] = np.nan
df.loc[np.random.choice(df.index, 15), 'Social_Media_Hours'] = np.nan

# Save to CSV
df.to_csv("mobile_usage_academic_performance.csv", index=False)
print(f"Dataset created and saved to mobile_usage_academic_performance.csv. Shape: {df.shape}")

# 2. Analysis & Visualization
plt.figure(figsize=(15, 12))

# Subplot 1: Data Size
plt.subplot(2, 2, 1)
size_metrics = {'Total Records': len(df), 'Total Features': len(df.columns)}
plt.bar(size_metrics.keys(), size_metrics.values(), color=['teal', 'coral'])
plt.title('Dataset Size Overview')
for i, v in enumerate(size_metrics.values()):
    plt.text(i, v + 5, str(v), ha='center')

# Subplot 2: Missing Values
plt.subplot(2, 2, 2)
missing = df.isnull().sum()
missing.plot(kind='bar', color='red', alpha=0.7)
plt.title('Missing Values Count per Feature')
plt.xticks(rotation=45)

# Subplot 3: Correlation Matrix
plt.subplot(2, 2, 3)
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('Correlation: Mobile Usage vs Performance')

# Subplot 4: Mobile Usage vs Exam Score (Regression Plot)
plt.subplot(2, 2, 4)
sns.regplot(x='Mobile_Usage_Hours', y='Exam_Score', data=df, 
            scatter_kws={'alpha':0.3, 'color':'blue'}, line_kws={'color':'red'})
plt.title('Trend: Mobile Usage vs Exam Score')

plt.tight_layout()
plt.savefig('academic_performance_analysis.png')
print("Analysis complete. Visualization saved as 'academic_performance_analysis.png'.")

# Print Summary
print("\n--- DATASET FEATURES ---")
print(f"Features: {list(df.columns)}")
print(f"Input Features: {list(df.columns[:-1])}")
print(f"Target Output: Exam_Score")
print("\n--- MISSING VALUES ---")
print(df.isnull().sum()[df.isnull().sum() > 0])
