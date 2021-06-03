import itertools
import numpy as np

##
# 12

x0 = 0.2
h = 0.2
N = 5
#

# ay'(x0) = b
# cy(xN) + dy'(xN) = e
a = 1
b = 0
c = 1.6
d = 1.4
e = 2.1


#

# y'' + p(x)y' + q(x)y = f(x)
def p(x):
    return 1 / x


def q(x=None):
    return -1.5


def f(x):
    return -x


##

def x(i):
    return x0 + i * h


def A():
    A = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    n = len(A)
    A[0][0:2] = -1, 1
    A[n - 1][n - 2:n] = -d, (d + h * c)
    for i in range(2, n):
        A[i - 1][i - 2:i + 1] = 1 + p(x(i)) + q(x(i)) * h ** 2, -2 - p(x(i)) * h, 1
    return A


def B():
    B = [0 for _ in range(N + 1)]
    B[0] = h * b / a
    B[len(B) - 1] = e * h
    for i in range(1, len(B) - 1):
        B[i] = f(x(i + 1)) * h ** 2

    return B


def get_x_points():
    return np.linspace(x0, x0 + h * N, N + 1)


def finite_differences_method():
    return (np.linalg.solve(A(), B()))


if (__name__ == "__main__"):
    print(np.array(A()))
    print(B())
    print(np.linalg.solve(A(), B()))
