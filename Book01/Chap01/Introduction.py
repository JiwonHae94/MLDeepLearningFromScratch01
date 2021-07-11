
def arithmetic():
    print(1+2)

def getType(var1):
    return type(var1)

def getListFromLeft(var1, index):
    return var1[index:]

def getListFromRight(var1 , index):
    return var1[:index]

if __name__ == '__main__':
    arithmetic()
    type1 = getType('test')
    type2 = getType(123)

    print(type1, type2)


    list1 = [1,2,3,4,5,6,7]
    print(list1)
    l1 = getListFromLeft(list1, 2)
    l2 = getListFromLeft(list1, 3)
    l3 = getListFromLeft(list1, 4)
    print(l1,l2,l3)

    list1 = [1,2,3,4,5,6,7]
    l1 = getListFromRight(list1, 2)
    l2 = getListFromRight(list1, 3)
    l3 = getListFromRight(list1, 4)
    print(l1, l2, l3)

    l1 = getListFromRight(list1, -2)
    l2 = getListFromRight(list1, -3)
    l3 = getListFromRight(list1, -4)
    print(l1, l2, l3)

    print(list1[:])
