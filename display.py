from finite_differences_method import finite_differences_method, get_x_points
import numpy as np
import matplotlib.pyplot as plt

## depends on specific values in matrix_operations !!!

def draw_plot(ys):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.grid(True)
    ax.plot(get_x_points(), ys, color='blue', marker='*')
    plt.show()
    plt.close()


print("finite differences method")
print(finite_differences_method())
draw_plot(finite_differences_method())
