class Sample:
    def __init__(self):
        self.name = "sample"
        self.initial = 0

    def add(self, var1):
        self.initial += var1
        return self.initial

    def substract(self, var1):
        self.initial -= var1
        return self.initial



if __name__ == '__main__':
    sample1 = Sample()
    print(sample1.initial)
    sample1.add(4)
    print(sample1.initial)
    sample1.substract(4)
    print(sample1.initial)
