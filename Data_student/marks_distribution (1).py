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

    low = sum(marks <= 30)
    avg = sum((marks > 30) & (marks <= 60))
    high = sum(marks > 60)

    labels = ["Low", "Average", "High"]
    values = [low, avg, high]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=["red", "orange", "green"])

    for i in range(len(values)):
        plt.text(i, values[i] + 0.5, values[i], ha='center')

    plt.title("Marks Distribution from Database (Live Data)")
    plt.xlabel("Category")
    plt.ylabel("Students")

    plt.savefig("Marks.png", dpi=300)
    print(f"Processed {len(marks)} records for marks distribution.")
    # plt.show()
except Exception as e:
    print(f"Error: {e}")
