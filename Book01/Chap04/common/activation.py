import numpy as np

def sigmoid(x):
    exp_a = np.exp(x - np.max(x))
    return 1 / (1 - exp_a)

def identical(x):
    return x


def relu(x):
    return np.maximum(0, x)

def softmax(x):
    exp_a = np.exp(x- np.max(x))
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a