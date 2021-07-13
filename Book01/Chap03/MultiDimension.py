import numpy as np
import matplotlib.pylab as plt

def get_ndim(x1):
    return np.ndim(x1)

def get_shape(x1):
    return np.shape(x1)

def matrixMultiplication(x1, x2):
    return np.dot(x1, x2)


if __name__ == '__main__':
    x1 = np.array([[1, 2], [3, 4]])
    r1 = get_ndim(x1)
    s1 = get_shape(x1)
    print(x1)
    print(r1, s1)


    x2 = np.array([[5,6],[7,8]])
    r2 = get_ndim(x2)
    s2 = get_shape(x2)
    print("\n", x2)
    print(r2, s2)

    dot = matrixMultiplication(x1, x2)
    print("\n", dot)