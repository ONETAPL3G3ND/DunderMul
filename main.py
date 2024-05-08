class Test:
    def __init__(self):
        self.value = 10

    def __mul__(self, other):
        self.value *= other

if __name__ == '__main__':
    a = Test()
    a * 10
    print(a.value)