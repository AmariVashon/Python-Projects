import os
import csv
import glob
import pandas as pd

if not glob.glob('cart.csv'):
    df = pd.DataFrame(columns = ['Item'])
    df.to_csv('cart.csv', index=False)


cart = []

def clear_screen():
    os.system('cls')

def addItem(item):
    clear_screen()
    cart.append(item)
    print(f"{item} has been added")

def removeItem(item):
    clear_screen()
    try:
        print(f"{item} has been removed")
    except:
        print("Sorry, that item could not be removed.")

def showCart():
    clear_screen()
    if cart:
        print("Here is your cart: ")
        for item in cart:
            print(f"- {item}")
    else:
        print("Your cart is empty.")

def saveCart():
    if cart:
        with open('cart.csv', 'a', newline="") as fid:
            writer = csv.writer(fid, delimiter=',')
            for item in cart:
                writer.writerow([item])
        clear_screen()
        print("Your cart has been saved!")

def clearCart():
    clear_screen()
    cart.clear()
    clear_cart = pd.DataFrame(columns = ["Item"])
    clear_cart.to_csv('cart.csv', index=False)
    print("Your cart is empty.")

def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/save/clear: ").lower()
        
        # base case
        if ans == "quit":
            print("Thanks for using our program.")
            showCart()
            done = True
        elif ans == "add":
            item = input("What item would you like to add? ")
            addItem(item)
        elif ans == "remove":
            item = input("What item would you like to remove? ")
            removeItem(item)
        elif ans == "show":
            showCart()
        elif ans == "save":
            saveCart()
        elif ans == "clear":
            clearCart()
        else:
            print("That was not an option.")

main()