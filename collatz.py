import sys

def collatz(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        print(num//2)
        return collatz(num//2)
    else:
        print(3 * num + 1)
        return collatz(3 * num + 1)

run = True
while run:
    ans = int(input("Input a number for the collatz sequence (0 to stop): "))
    if ans == 0:
        sys.exit()
    while collatz(ans) != 1:
        collatz(ans)
        if collatz(ans) == 1:
            run = False
