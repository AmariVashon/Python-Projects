def create_phone_number(n):
    #your code here
    character = ""
    
    first_digits = []
    for i in range(3):
        first_digits.append(f"{n[i]}")
    
    first_join = character.join(first_digits)
    
    second_digits = []
    for i in range(3, 6):
        second_digits.append(f"{n[i]}")
    
    second_join = character.join(second_digits)
    
    third_digits = []
    for i in range(6, 10):
        third_digits.append(f"{n[i]}")
    
    third_join = character.join(third_digits)
    
    combine = "(" + first_join + ") " + second_join + "-" + third_join
    
    return combine
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(n))

def make_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(make_phone_number(n))