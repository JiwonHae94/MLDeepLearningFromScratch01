import numpy as np
import sys, os

from dataset.mnist import load_mnist

sys.path.append(os.pardir)
from common.activation import *
from internal.loader import load_weights
from common.loss import *

class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entry_loss(y, t)

        return loss

def f(W):
    return net.loss()

if __name__ == '__main__':
    net = SimpleNet()
    print(net.W)

    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print(p)
    print(np.argmax(p))

    t =  np.array([0, 0, 1])
    rslt = net.loss(x, t)
    print(rslt)