import numpy as np
import matplotlib.pyplot as plt

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1 * w2 + w2 * x2
    if temp <= theta:
        return 0
    else:
        return 1

def AND_NP(x1):
    w, b = np.array([0.5, 0.5]), -0.7
    temp = np.sum(w * x1) + b

    if temp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    temp = x1 * w2 + w2 * x2
    if temp <= theta:
        return 0
    else:
        return 1

def NAND_NP(x1):
    w, b = np.array([-0.5, -0.5]), 0.7
    temp = np.sum(w * x1) + b

    if temp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, .2

    temp = x1 * w2 + w2 * x2
    if temp <= theta:
        return 0
    else:
        return 1

def OR_NP(x1):
    w, b = np.array([0.5, 0.5]), -0.2
    temp = np.sum(w * x1) + b

    if temp <= 0:
        return 0
    else:
        return 1

def XOR_NP(x1):
    s1 = NAND_NP(x1)
    s2 = OR_NP(x1)
    y = AND_NP(np.array([s1, s2]))
    return y

if __name__ == '__main__':
    temp1 = AND(0,0)
    temp2 = AND(1,0)
    temp3 = AND(0,1)
    temp4 = AND(1,1)

    np_temp1 = AND_NP(np.array([0, 0]))
    np_temp2 = AND_NP(np.array([1, 0]))
    np_temp3 = AND_NP(np.array([0, 1]))
    np_temp4 = AND_NP(np.array([1, 1]))

    print(temp1, temp2, temp3, temp4)
    print(np_temp1, np_temp2, np_temp3, np_temp4)

    temp1 = NAND(0, 0)
    temp2 = NAND(1, 0)
    temp3 = NAND(0, 1)
    temp4 = NAND(1, 1)

    np_temp1 = NAND_NP(np.array([0, 0]))
    np_temp2 = NAND_NP(np.array([1, 0]))
    np_temp3 = NAND_NP(np.array([0, 1]))
    np_temp4 = NAND_NP(np.array([1, 1]))

    print(temp1, temp2, temp3, temp4)
    print(np_temp1, np_temp2, np_temp3, np_temp4)

    temp1 = OR(0,0)
    temp2 = OR(1,0)
    temp3 = OR(0,1)
    temp4 = OR(1,1)

    np_temp1 = OR_NP(np.array([0, 0]))
    np_temp2 = OR_NP(np.array([1, 0]))
    np_temp3 = OR_NP(np.array([0, 1]))
    np_temp4 = OR_NP(np.array([1, 1]))

    print(temp1, temp2, temp3, temp4)
    print(np_temp1, np_temp2, np_temp3, np_temp4)

    np_temp1 = XOR_NP(np.array([0, 0]))
    np_temp2 = XOR_NP(np.array([1, 0]))
    np_temp3 = XOR_NP(np.array([0, 1]))
    np_temp4 = XOR_NP(np.array([1, 1]))

    print("XOR", np_temp1, np_temp2, np_temp3, np_temp4)
