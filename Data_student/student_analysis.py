import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("student_performance.csv")

# 2. Calculate average score
df["Average_Score"] = (df["Math_Score"] + df["Reading_Score"] + df["Writing_Score"]) / 3

# 3. Create a new column for Mobile Usage based on average score (Simulated)
# Higher scores generally linked to lower simulated mobile usage in this logic
def simulate_mobile(score):
    if score > 80: return 2
    if score > 60: return 4
    if score > 40: return 6
    return 8

df["Simulated_Mobile_Usage"] = df["Average_Score"].apply(simulate_mobile)

# Determine Performance Category for charts
def get_performance(score):
    if score > 70: return "High"
    if score > 40: return "Medium"
    return "Low"

df["Performance_Category"] = df["Average_Score"].apply(get_performance)

# Set plotting style
plt.style.use('ggplot')

# --- Visualization 1: Bar Chart (Distribution of Student Performance) ---
plt.figure(figsize=(8, 5))
performance_counts = df["Performance_Category"].value_counts().reindex(["High", "Medium", "Low"])
performance_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Distribution of Student Performance")
plt.xlabel("Performance Category")
plt.ylabel("Number of Students")
plt.savefig("performance_bar_chart.png")
print("Saved performance_bar_chart.png")

# --- Visualization 2: Line Chart (Trend of Average Scores) ---
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["Average_Score"], color='blue', linewidth=1)
plt.title("Trend of Average Scores Across Students")
plt.xlabel("Student Index")
plt.ylabel("Average Score")
plt.savefig("score_trend_line_chart.png")
print("Saved score_trend_line_chart.png")

# --- Visualization 3: Pie Chart (Percentage Distribution) ---
plt.figure(figsize=(7, 7))
plt.pie(performance_counts, labels=performance_counts.index, autopct='%1.1f%%', colors=['green', 'orange', 'red'], startangle=140)
plt.title("Percentage Distribution of Performance Categories")
plt.savefig("performance_pie_chart.png")
print("Saved performance_pie_chart.png")

# Display final info
print(f"\nAnalysis complete. Processed {len(df)} students.")
