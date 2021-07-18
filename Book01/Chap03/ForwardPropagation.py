import numpy as np
import matplotlib.pylab as plt
import sys, os
sys.path.append(os.pardir)
import pickle

from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    image = Image.fromarray(np.uint8(img))
    image.show()

def get_data():
    (x_train, t_train) , (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    return x_test, t_test

def init_network() :
    with open("sample_weight.pkl", "rb") as f :
        network = pickle.load(f)

    return network

def sigmoid(x):
    overflow = x - np.max(x)
    return 1/ (1 + np.exp(overflow))


def identical(x):
    return x

def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

def inference(x, t, network):
    acc_cnt = 0

    for i in range(1):
        y = predict(network, x)
        p = np.max(y)

        if p == t[i]:
            acc_cnt += 1

        print("progress : " + str(i) + "/" + str(len(x)))


def inference_batch(x, t, network):
    acc_cnt = 0
    batch_size = 100

    for i in range(0, len(x), batch_size):
        x_batch = x[i:i+batch_size]
        y_batch = predict(network, x_batch)
        p = np.argmax(y_batch, axis = 1)
        acc_cnt += np.sum(p == t[i:i+batch_size])
        print("progress : " + str(i / batch_size) + "/" + str(len(x)/batch_size))

    print("accuracy : " + str(float(acc_cnt) / len(x)))

if __name__ == '__main__':
    x, t = get_data()
    network = init_network()

    inference_batch(x,t, network)




