import numpy as np

# mean square error
# t : ground truth
# y : output
def mse(t : np.array, y : np.array):
    return np.sum((y-t) ** 2) / 5

# cross entropy loss
# t : ground truth
# y : output
def cee(y : np.array, t:np.array):
    delta = 1e-7
    return -1 * np.sum(t * np.log(y + delta))

def cee_batch(y : np.array, t:np.array):
    if y.dim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum( t * np.log(y + 1e-7)) / batch_size