import numpy as np

def mean_squared_error(y, t):
    return np.sum(np.square(y-t)) / 2

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x-np.max(x, axis = 0)
        y = np.exp(x) / np.sum(np.exp(x), axis = 0)
        return y.T

    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))
