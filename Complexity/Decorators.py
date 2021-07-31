def decorator(func):
    def wrap():
        num = int(input("Input a number: "))
        if num < 100:
            func()
    return wrap

@decorator
def numbers():
    print("Less than 100")

numbers()

print("\n")

def route(string):
    def wrap(func):
        print(string)
        func()
    return wrap

@route("/index")
def index():
    print("This is how web pages are made in Flask")
