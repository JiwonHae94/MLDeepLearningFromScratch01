import numpy as np

from common.common import numerical_gradient
from common.loss import cee
from common.output import softmax


class simpleNet:
    def __init__(self):
        self.W  = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)


    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cee(y, t)

        return loss

net = simpleNet()
print(net.W)

x = np.array([.6, .9])
p = net.predict(x)
print(p)

t = np.array([0, 0, 1])
net.loss(x, t)

def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)