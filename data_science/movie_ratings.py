num_people, rating = [0, 0, 0, 0, 0], [1, 2, 3, 4, 5]

run = True
while run:
    try:
        answer = int(input("What would you rate this movie (1-5)? "))
    except:
        print("Please input an integer.")
    
    if answer == 1:
        num_people[0] += 1
    elif answer == 2:
        num_people[1] += 1
    elif answer == 3:
        num_people[2] += 1
    elif answer == 4:
        num_people[3] += 1
    elif answer == 5:
        num_people[4] += 1
    else:
        print("Not a valid rating.")
        
    try: 
        cont = str(input("Is there another user that would like to review (y/n)? "))
    except:
        print("Invalid input")
    
    if cont == "n":
        run = False

plt.bar(rating, num_people)

plt.title("Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("# of People")

plt.show()
