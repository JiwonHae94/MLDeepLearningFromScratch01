import numpy as np

from common.gradient import gradient_descent


def function_2(x):
    return x[0] ** 2 + x[1] ** 2

if __name__ == '__main__':
    init_x = np.array([-3.0, 4.0])
    rslt = gradient_descent(function_2, init_x = init_x, lr = 0.1, step_num = 100)
    print(rslt)