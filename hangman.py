# Written by Amari
# For educational purposes only

import random

# These are just a few things I came up with in order to have phrases instead of single words
# You can also add a txt file with a huge list of words and have this program randomly pick a word from that file
words = ["Diary Of a Wimpy Kid", "The Avengers", "United States of America", "Kendrick Lamar"]
words = random.choice(words)

x = words.replace(" ", "")

guess = 0
inp = []
complete = False

print("""Welcome to Hangman. The computer has generated a word/phrase, and it is up to you to figure out if this word/phrase contains a specific letter. 
If the letter is not in the word/phrase, then a part of hangman is added. You can only guess incorrectly 6 times.""")

while not complete:
    for letter in words:
        if letter is " ":
            print(" ", end=" ")
        if letter.lower() in inp:
            print(letter, end=" ")
        elif (letter.lower() not in inp) and (letter is not " "):
            print("_", end=" ")
    print("")

    guesses = input(f"Current guesses {inp}, guesses wrong: {guess}, next guess: ")
    inp.append(guesses.lower())
    if guesses.lower() not in x.lower():
        guess += 1
        if guess == 6:
            print(f"Current guesses {inp}, guesses wrong: {guess}")
            break

    complete = True
    for letter in x:
        if letter.lower() not in inp:
            complete = False

if complete:
    print(f"You guessed the word/phrase: {words}")
else:
    print(f"Game Over. The word/phrase was: {words}")
