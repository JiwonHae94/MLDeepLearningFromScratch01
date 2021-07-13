import numpy as np
import matplotlib.pylab as plt

# Activation functins
# 1) Sigmoid

def step_function(x):
    if x > 0:
        return 1
    else:
        return 1

def step_function_np(x):
    return np.array(x>0, dtype = np.int16)

def sigmoid(x):
    return 1/(np.exp(-x) +1)

def relu(x):
    return np.maximum(x, 0)

def plot(x1, y1):
    plt.plot(x1,y1)
    plt.ylim(-0.1, 1.1)
    plt.show()

def plot2(x1, y1, y2):
    plt.plot(x1,y1, label = "sigmoid")
    plt.plot(x1,y2, linestyle = "--", label = "step")
    plt.ylim(-.1, 1.1)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    x1 = np.array([-1.0, 2.0, 2.0])
    r1 = step_function_np(x1)
    x1 = np.arange(-5, 5, 0.1)
    y1 = step_function_np(x1)
    plot(x1, y1)

    y2 = sigmoid(x1)
    plot(x1, y2)
    plot2(x1, y2, y1)
    y3 = relu(x1)

    plot2(x1,y3,y2)
