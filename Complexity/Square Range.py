def range1(stop, start=0, step = 1, exponent = 2):
    while start < stop:
        yield start**exponent
        start += step

for x in range1(4):
    print(x)
