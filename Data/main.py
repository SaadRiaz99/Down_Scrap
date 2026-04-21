import matplotlib.pyplot as plt

print("Hello from data!")

def plot_data():
    x = [1, 2, 3, 4]
    y = [10, 20, 25, 30]


    plt.plot(x,y)
    plt.title('Sample Data')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.savefig('plot.png')  # Save instead of show
    print("Plot saved as plot.png")

plot_data()