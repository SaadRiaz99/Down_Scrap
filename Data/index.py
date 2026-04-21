import matplotlib.pyplot as plt


students = []
marks = []


n = int(input("How many Data you want to get? "))

def plot_student_marks():
    for i in range(n):
        name = input(f"Student {i + 1} Name:")
        mark = float(input(f"Student {i + 1} Marks:"))  # Convert to float

        students.append(name)
        marks.append(mark)

    # Calculate average
    if marks:
        avg = sum(marks) / len(marks)
    else:
        avg = 0

    # Plot after collecting all data
    plt.figure(figsize=(8,5))
    plt.bar(students, marks, color="skyblue")

    # Average line
    plt.axhline(avg, color="red", linestyle="--", label=f"Average = {avg:.2f}")

    plt.title("Student Performance Report")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.legend()

    plt.savefig('student_marks.png')  
    print("Plot saved as student_marks.png")

plot_student_marks()