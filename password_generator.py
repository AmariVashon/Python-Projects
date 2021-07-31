import random as rd

alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
alphabet.sort()

characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0',
               '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '*', '(', ')', '_', '+','?', ';', ':']


password = ""

for x in alphabet:
    characters.append(x.upper())

characters.sort()

count = 0

for x in range(3):
    for y in range(5):
        password += characters[rd.randint(0, len(characters) - 1)]
    count += 1
    if count < 3:
        password += "-"

print(password)

