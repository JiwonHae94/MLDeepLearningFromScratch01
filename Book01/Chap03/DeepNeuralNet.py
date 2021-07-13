import numpy as np
import matplotlib.pylab as plt

def layer1(X):
    W1 = np.array([[.1,.3,.5], [.2,.4,.6]])
    B1 = np.array([.1,.2,.3])

    return np.dot(X, W1) + B1

def sigmoid(x):
    return 1 / (1+np.exp(-x))

def layer2(X):
    W2 = np.array([[.1,.4],[.2,.5],[.3,.6]])
    B2 = np.array([.1,.2])

    return np.dot(X, W2) + B2

def layer3(X):
    W3 = np.array([[.1,.3],[.2,.4]])
    B3 = np.array([.1, .2])

    return np.dot(X, W3) + B3

def identity(X):
    return X

def softmax(x):
    # c is deducted from the initial method to prevent computational overflow
    c = np.max(x)
    return np.exp(x-c) / np.sum(np.exp(x-c))


def sampleNetwork():
    network = {}
    network["W1"] = np.array([[.1,.3,.5], [.2,.4,.6]])
    network["b1"] = np.array([.1,.2,.3])
    network["W2"] = np.array([[.1,.4],[.2,.5],[.3,.6]])
    network["b2"] = np.array([.1,.2])
    network["W3"] = np.array([[.1,.3],[.2,.4]])
    network["b3"] = np.array([.1, .2])

    ## forward
    x1 = np.array([1, .5])
    a1 = np.dot(x1, network["W1"]) + network["b1"]
    z1 = sigmoid(a1)
    a2 = np.dot(z1, network["W2"]) + network["b2"]
    z2 = sigmoid(a2)
    a3 = np.dot(z2, network["W3"]) + network["b3"]
    #z3 = sigmoid(a3)

    Y = softmax(a3)
    return Y



if __name__ == '__main__':
    X1 = np.array([1, .5])
    A1 = layer1(X1)
    Z1 = sigmoid(A1)

    A2 = layer2(Z1)
    Z2 = sigmoid(A2)

    A3 = layer3(Z2)
    Y = identity(A3)

    print(A1)
    print(Z1)

    print(A2)
    print(Z2)

    print(A3)
    print(Y)

    rslt = sampleNetwork()
    print("sample network", rslt)

    a = np.array([.3, 2.9, 4])
    exp_a = np.exp(a-np.max(a))
    print("softmax ", exp_a / np.sum(exp_a))


    a = np.array([1010, 1000, 990])
    exp_a = np.exp(a-np.max(a))
    print("softmax ", exp_a / np.sum(exp_a))