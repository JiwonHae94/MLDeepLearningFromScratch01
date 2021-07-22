from common.gradient import numerical_gradient, numerical_gradient_2d
import numpy as np

from common.loss import softmax, cross_entropy_error


class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y ,t)
        return loss

def f(W):
    return net.loss(x, t)

if __name__ == '__main__':
    net = SimpleNet()
    x = np.array([.6, .9])
    p = net.predict(x)

    print(p)
    print(np.argmax(p))

    t = np.array([0, 0, 1])
    loss = net.loss(x  , t)
    print(loss)

    dW = numerical_gradient_2d(f, net.W)
    print(dW)