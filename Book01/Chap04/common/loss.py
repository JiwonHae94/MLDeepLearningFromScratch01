import numpy as np

def mean_squared_error(y, t):
    return np.sum(np.square(y-t)) / 2

def cross_entry_loss(y, t):
    # delta is added to remove possibility of negative infinite from happening
    delta = 1e-7
    return -np.sum(t * np.log(y+ delta))

def cross_entry_loss_batch(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size