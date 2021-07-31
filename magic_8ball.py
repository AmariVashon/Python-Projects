import random as rd

phrases = ["It is certain", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", 
"As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", 
"Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", 
"Outlook not so good", "Very doubtful"]

print("Welcome to the magic 8 ball. Press enter to begin. Press Q to quit at any time.")
done = False

while not done:
    inp = str(input("Ask a question and I will answer: "))
    if inp.lower() == "q":
        done = True
        break
    print(phrases[rd.randint(0, len(phrases))])
