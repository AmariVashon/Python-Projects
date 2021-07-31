class RevIter():
    def __init__(self, aList):
        self.list = aList
    def __iter__(self):
        self.index = len(self.list) - 1
        return self
    def __next__(self):
        if self.index >= 0:
            char = self.list[self.index]
            self.index -= 1
            return char
        else:
            raise StopIteration
for i in RevIter([1, 2, 3, 4, 5]):
    print(i, end = ", ")
