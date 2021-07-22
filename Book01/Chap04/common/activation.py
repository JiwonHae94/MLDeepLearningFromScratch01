import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identical(x):
    return x


def relu(x):
    return np.maximum(0, x)
