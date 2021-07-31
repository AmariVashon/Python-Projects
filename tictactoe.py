board = {'1' : ' ', '2' : ' ', '3' : ' ',
         '4' : ' ', '5' : ' ', '6' : ' ',
         '7' : ' ', '8' : ' ', '9' : ' '}

mock_board = {'1' : '1', '2' : '2', '3' : '3',
              '4' : '4', '5' : '5', '6' : '6',
              '7' : '7', '8' : '8', '9' : '9'}
         
def print_board(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print("-+-+-")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-+-+-")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])


def Game():
    done = False
    turn = 'O'
    count = 0

    see = input(f"Player {turn} turn. Press b to see the board positions: ")
    if see.lower() == 'b':
        print_board(mock_board)
    
    print("\n")
    while not done:
        print_board(board)

        place = int(input("Select a position on the board (1-9): "))
        if board[f"{place}"] == ' ':
            board[f"{place}"] = turn
            count += 1
        else:
            print("That spot is filled. Try again")
            continue

        if count >= 5:
            if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O':
                print_board(board)
                print("Player O has won!")
                done = True
            elif board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
            elif board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
                print_board(board)
                print("Player X has won!")
                done = True
        
        if count == 9 and not done:
            print_board(board)
            print("It's a tie!")
            done = True

        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'
        
    restart = input("Do you want to play again? (y/n) ")
    if restart.lower() == 'y':
        for i in board:
            board[i] = " "
        Game()
        


Game()