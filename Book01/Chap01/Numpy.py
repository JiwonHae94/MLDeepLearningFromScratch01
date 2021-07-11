import numpy as np

def createArray(arr):
    return np.array(arr)

def addition(x, y):
    return np.add(x,y)

def substractoin(x, y):
    return np.subtract(x,y)


if __name__ == '__main__':
    createArray([1,2,3])

    x = createArray([1,2,3])
    y = createArray([3,4,5])

    print(x+y)
    print(addition(x,y))

    print(x-y)
    print(substractoin(x, y))

    doubleArray1 = createArray([[1, 2], [3,4]])
    doubleArray2 = createArray([[4, 5],[5,6,],[7,8]])

    print(doubleArray1 + doubleArray2)