import csv
import os
import pandas as pd
import glob

if not glob.glob('user.csv'):
    df = pd.DataFrame(columns = ['email', 'password'])
    df.to_csv('user.csv', index=False)

def clear_screen():
    os.system('cls')

def checkRegister(email):
    df = pd.read_csv('user.csv')
    for i in df.values.tolist():
        for j in i:
            if email == j:
                return True
    return False

def registerUser():
    with open('user.csv', 'a', newline="") as fid:
        writer = csv.writer(fid, delimiter=',')
        print("To register, please enter your info: ")
        email = input("Enter your email: ")
        if checkRegister(email):
            print("This email is already registered!")
        else:
            password = input("Enter your password: ")
            password2 = input("Enter your password again: ")
            clear_screen()
            if password == password2:
                writer.writerow([email, password])
                print("You are now registered!")
            else:
                print("Your passwords do not match. Try again.")

def loginUser():
    print("To login, please enter your info: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    clear_screen()
    with open('user.csv', 'r') as fid:
        reader = csv.reader(fid, delimiter=',')
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                return True
    print("Something went wrong. Try again.")
    return False

def changePassword():
    try:
        df = pd.read_csv('user.csv')
        email = input("Confirm your email: ")
        new_password = input("Enter your new password: ")
        new_password2 = input("Enter your new password again: ")
        if new_password == new_password2:
            df.loc[df['email'] == email,'password'] = new_password
            df.to_csv('user.csv', index=False)
            clear_screen()
            print("Your password has been changed!")
    except:
        print("Error")



def main():
    run = True
    logged_in = False

    while run:
        if logged_in:
            print("1. Logout\n2. Change Password\n3. Quit")
        else:
            print("1. Login\n2. Register\n3. Quit")
        
        choice = input("What would you like to do? ").lower()
        if choice == 'register' and logged_in == False:
            registerUser()
        elif choice == 'login' and logged_in == False:
            logged_in = loginUser()
        elif choice == "change password" and logged_in == True:
            changePassword()
        elif choice == "quit":
            run = False
            print("Thanks for using this!")
        elif choice == "logout" and logged_in == True:
            logged_in = False
            print("You are now logged out.")
        else:
            print("Please try again.")

main()