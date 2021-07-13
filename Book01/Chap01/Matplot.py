import numpy as np
import matplotlib.pyplot as plt

def draw(x,y):
    plt.plot(x,y)
    plt.show()

def drawComplex(x, y1, y2):
    plt.plot(x, y1, label= "sin")
    plt.plot(x, y2, linestyle = "--", label = "cos")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("sin & cos")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    x = np.arange(0, 6 , 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    drawComplex(x,y1,y2)