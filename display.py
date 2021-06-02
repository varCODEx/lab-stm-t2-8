from matrix_operations import *
import numpy as np
import matplotlib.pyplot as plt

## depends on specific values in matrix_operations !!!

def xs():
    return np.linspace(x0, x0+h*n, n+1)



def draw_plot(ys):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.grid(True)
    ax.plot(xs(), ys, color='blue', marker='o')
    plt.show()
    plt.close()


print("finite differences method")
print(jacobian(np.array(mx_coefficients()), np.array(matrix_w_coefficients())))
draw_plot(jacobian(np.array(mx_coefficients()), np.array(matrix_w_coefficients())))
