from random import choice

choices = ['rock', 'paper', 'scissors']

run = True
count = 0
scores = {'user': 0, 'computer': 0, 'ties': 0}

while run == True:
    comp_choice = choice(choices)

    if count == 0:
        prompt = "Welcome to rock, paper, scissors\nPress 0 to quit\nRock, paper, or scissors? "
        user_choice = str(input(prompt))
        count += 1
    else:
        prompt = "Rock, paper, or scissors? "
        user_choice = str(input(prompt))

    if (user_choice.lower() == comp_choice):
        print(f"Tie! The computer also chose {user_choice}!")
        scores['ties'] += 1
        continue
    elif (user_choice.lower() == 'rock') and (comp_choice == 'paper'):
        print("You lost! The computer chose paper!")
        scores['computer'] += 1
        continue
    elif (user_choice.lower() == 'rock') and (comp_choice == 'scissors'):
        print("You won! The computer chose scissors!")
        scores['user'] += 1
        continue
    elif (user_choice.lower() == 'paper') and (comp_choice == 'rock'):
        print("You won! The computer chose rock!")
        scores['user'] += 1
        continue
    elif (user_choice.lower() == 'paper') and (comp_choice == 'scissors'):
        print("You lost! The computer chose scissors!")
        scores['computer'] += 1
        continue
    elif (user_choice.lower() == 'scissors') and (comp_choice == 'rock'):
        print("You lost! The computer chose rock!")
        scores['computer'] += 1
        continue
    elif (user_choice.lower() == 'scissors') and (comp_choice == 'paper'):
        print("You won! The computer chose paper!")
        scores['user'] += 1
        continue
    elif (user_choice == '0'):
        print(f"Thanks for playing. The final score was:\nyou: {scores['user']}\ncomputer: {scores['computer']}\nties: {scores['ties']}")
        run = False
    else:
        print("Invalid choice. Try again")
        continue
