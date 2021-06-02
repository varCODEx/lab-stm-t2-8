import itertools
import numpy as np

##
# 12
x0 = 0.2
h = 0.2
c1 = 0
c2 = 1
c = 1
d1 = 1.6
d2 = 1.4
d = 2.1
n = 5


def p():
    return 1


def q(x):
    return -1.5 * x


def f():
    return 0


##

def mx_coefficients():
    def init_zeros():
        temp_matrix = []
        for i in range(n + 1):
            temp_matrix.append(list(itertools.repeat(0, n + 1)))
        return temp_matrix

    def fill_matrix(matrix):
        x = x0
        values = [c1 * h + c2, c2, 0, 0, -d2, d1 * h + d2]
        index = 0
        for i in range(len(matrix)):
            if i % n == 0:
                for j in range(len(matrix)):
                    if j <= i + 1 and i == 0:
                        matrix[i][j] = values[j]
                    elif n - 2 <= j <= i + 1:
                        matrix[i][j] = values[j]
            else:
                matrix[i][index] = 1 - (p() * h) / 2
                matrix[i][index + 1] = q(x) * h ** 2 - 2
                matrix[i][index + 2] = 1 + (p() * h) / 2
                index += 1
            x += h
        return matrix

    return fill_matrix(init_zeros())


def matrix_w_coefficients():
    def init_zeros():
        temp_matrix = []
        for i in range(n + 1):
            temp_matrix.append(0)
        return temp_matrix

    def fill_matrix(matrix):
        matrix[0] = c * h
        for i in range(1, len(matrix)):
            matrix[i] = f() * h ** 2

        matrix[len(matrix) - 1] = d * h
        return matrix

    return fill_matrix(init_zeros())


def jacobian(a, b):
    x = np.zeros_like(b)
    for it_count in range(100):
        x_new = np.zeros_like(x)

        for i in range(a.shape[0]):
            s1 = np.dot(a[i, :i], x[:i])
            s2 = np.dot(a[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / a[i, i]
            if x_new[i] == x_new[i - 1]:
                break
        # if np.allclose(x, x_new, atol=1e-10, rtol=0.):
        #     break
        x = x_new
    return x

