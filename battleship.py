print("Welcome to Battleship!")

board = []

for c in range(0, 10):
    board.append(["-"] * 10)


def print_board(board):
    for x in board:
        print(" ".join(x))


def addShip(row, col, length, horizontal):
    if (row >= len(board)) or (row < 0) or (col >= len(board[0])) or (col < 0):
        return False
    if horizontal:
        if col + length > len(board):
            return False
        for i in range(col, col + length):
            if board[row][i] != "-":
                return False
        for i in range(col, col + length):
            board[row][i] = "b"
    else:
        if row + length > len(board):
            return False
        for i in range(row, row + length):
            if board[i][col] != "-":
                return False
        for i in range(row, row + length):
            board[i][col] = "b"
    return True


def foundShip(length):
    for i in range(0, len(board)):
        count = 0
        while count < len(board[0]):
            a = 0
            while board[i][count] == "b":
                count += 1
                a += 1
            if a == length:
                return True
            a = 0
            count += 1
    for x in range(0, len(board[0])):
        count = 0
        while count < len(board):
            a = 0
            while board[count][x] == "b":
                a += 1
                count += 1
            if a == length:
                return True
            a = 0
            count += 1
    return False


def shoot(row, col):
    if (row < 0) or (row >= len(board)) or (col < 0) or (col >= len(board[0])):
        return -1
    if board[row][col] == "-":
        board[row][col] = "m"
        return 0
    if board[row][col] == "b":
        board[row][col] = "x"
        return 1
    if (board[row][col] == "x") or (board[row][col] == "m"):
        return 2
    return 0


def gameOver():
    for i in range(0, len(board)):
        for y in range(0, len(board[0])):
            if board[i][y] == "b":
                return False
    return True


addNew = True

while addNew:
    ans = input("Type \"a\" to add new ship, \"b\" to see the board, \"p\" to play or \"q\" to quit.\n")
    if ans.lower() == "q":
        break
    if ans.lower() == "a":
        r = int(input("Starting in which row? "))
        c = int(input("Starting in which column? "))
        l = int(input("How long? "))
        d = str(input("Horizontal (h) or vertical (v)? "))
        h = bool(d.lower() == "h")

        if addShip(r, c, l, h):
            print("New ship added!")
        else:
            print("Can't put a ship there!")
    if ans.lower() == "b":
        print_board(board)
    if ans.lower() == "p":
        if foundShip(3) and foundShip(4):
            addNew = False
            print("Ok, let's play!")
        else:
            print("You need ships of length 3 and 4 to play!")
while not gameOver():
    ans = input("Press \"s\" to shoot at a square, \"b\" to see the board, \"q\" to quit.\n")
    if ans.lower() == "q":
        break
    if ans.lower() == "s":
        r = int(input("Enter row: "))
        c = int(input("Enter column: "))

        result = shoot(r, c)

        if result == 1:
            print("Hit!")
        elif result == 0:
            print("Miss!")
        elif result == 2:
            print("You already tried that")
        elif result == -1:
            print("Invalid coordinates")
    if ans.lower() == "b":
        print_board(board)

print("Game over!")
