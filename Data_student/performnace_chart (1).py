import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\python\project\Data_student\dbms assigemnt no 2 (2).accdb;'

try:
    conn = pyodbc.connect(conn_str)
    query = "SELECT Marks FROM student_performance"
    df = pd.read_sql(query, conn)
    conn.close()

    marks = df["Marks"].dropna()

    high = sum(marks > 60)
    medium = sum((marks > 30) & (marks <= 60))
    low = sum(marks <= 30)

    labels = ["High", "Medium", "Low"]
    counts = [high, medium, low]

    plt.figure(figsize=(8, 8))
    plt.pie(counts, labels=labels, autopct='%1.1f%%',
            colors=["green", "yellow", "red"])

    plt.title("Student Performance Distribution (Live Data)")

    plt.savefig("performance_distribution.png", dpi=300)
    print(f"Processed {len(marks)} records for performance chart.")
    # plt.show()
except Exception as e:
    print(f"Error: {e}")
