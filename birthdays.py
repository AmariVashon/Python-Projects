import pandas as pd
import glob

# dictionary for name : name, birthday : birthday key-value pairs
birthdays = {}

# if the file "birthdays.csv" exists, names and birthdays will be generated from the existing DataFrame, else, create new lists
if glob.glob('birthdays.csv'):
    df = pd.read_csv('birthdays.csv')
    names = df["names"].tolist()
    birthday = df["birthday"].tolist()
else:
    names = []
    birthday = []

# check if someone's name is already in DataBase
def checkBirthday(name):
    if name in names:
        return True
    return False

# add someone's birthday by adding their name and birthday to dictionary, converting dictionary to DataFrame, then saving it by exporting to CSV
def addBirthday(name, bday):
    names.append(name)
    birthday.append(bday)

    birthdays = {"names" : names, "birthday" : birthday}

    print(f"{name}'s birthday has been added! ")

    df = pd.DataFrame.from_dict(birthdays)
    df.to_csv("birthdays.csv")

# Delete name and birthday from database (work in progress)
def deleteBirthday(name):
    pass

run = True

while run:
    try:
        ans = str(input("Would you like to add (a) a birthday, search (s) for a birthday, or quit (q)? "))
    except:
        print("Please input a correct value.")
    
    if ans.lower() == "add" or ans.lower() == "a":
        name = input("Who would you like to add? ")
        if checkBirthday(name):
            exist = input("This person already exists. Would you like to search for their birthday (y/n)? ")
            if exist == "y":
                print(f"{name}'s birthday is on {birthday[names.index(name)]}")
            else:
                continue
        else:
            bday = input("When is their birthday? ")
            addBirthday(name, bday)
    elif ans.lower() == "search" or ans.lower() == "s":
        name = input("Enter a name to search: ")
        if checkBirthday(name):
            print(f"{name}'s birthday is on {birthday[names.index(name)]}")
        else:
            add = input("I could not find the name. Would you like to add their birthday (y/n)? ")
            if add == "y":
                bday = input("What is their birthday? ")
                addBirthday(name, bday)
            else:
                continue
    elif ans.lower() == "quit" or ans.lower() == "q":
        run = False
        print('Thank you for using this tool!')
