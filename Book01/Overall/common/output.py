import numpy as np

def identity(x):
    return x

def softmax(x : np.array):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_x = np.sum(x)

    return exp_x / sum_x