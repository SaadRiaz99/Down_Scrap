import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Database connection string
conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\python\project\Data_student\dbms assigemnt no 2 (2).accdb;'

try:
    # Connect to the database
    conn = pyodbc.connect(conn_str)
    
    # Read data into pandas DataFrame
    query = "SELECT * FROM student_performance"
    df = pd.read_sql(query, conn)
    conn.close()

    # Use 'Marks' as the score
    df["average_score"] = df["Marks"]

    plt.figure(figsize=(10, 6))
    plt.scatter(df["Mobile_Hours"], df["average_score"], color="blue", alpha=0.5)

    plt.title("Mobile Usage vs Academic Performance (Live Data)")
    plt.xlabel("Mobile Usage (Hours)")
    plt.ylabel("Average Score")

    plt.grid(True)
    plt.savefig("real_mobile_vs_marks.png", dpi=300)
    print(f"Successfully processed {len(df)} records from database.")
    # plt.show() # Commented out for non-interactive execution
except Exception as e:
    print(f"Error: {e}")
