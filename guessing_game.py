import random
def main():
    computer = int(random.random() * 100)
    inp = int(input("The computer is thinking of a number between 0 and 100. Try and guess it: "))
    guess = 0
    while (inp >= 0):
        if (computer == inp):
            print("Correct! You guessed it in " + str(guess) + " tries")
            break
        elif (inp > computer):
            guess += 1
            print("Too high. Try again")
            inp = int(input())
        elif (inp < computer):
            guess += 1
            print("Too low. Try again")
            inp = int(input())

main()
