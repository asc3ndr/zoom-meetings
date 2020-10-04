def print_board(board):  # [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print(f"-+-+-")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print(f"-+-+-")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")


def check_winner(board, ostepop):
    if board[0][0] == board[0][1] == board[0][2] == ostepop:
        return True
    elif board[1][0] == board[1][1] == board[1][2] == ostepop:
        return True
    elif board[2][0] == board[2][1] == board[2][2] == ostepop:
        return True
    elif board[0][0] == board[1][0] == board[2][0] == ostepop:
        return True
    elif board[0][1] == board[1][1] == board[2][1] == ostepop:
        return True
    elif board[0][2] == board[1][2] == board[2][2] == ostepop:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == ostepop:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == ostepop:
        return True
    return False


def update_board(board, row, col, current_player):
    board[row][col] = current_player


def verify_entry(board, row, col):
    if row < 0 or row > 2:
        return False
    if col < 0 or col > 2:
        return False
    if board[row][col] != " ":
        return False
    return True


brett = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_board(brett)  # prints an empty board
current = None
moves = 0
while moves < 9 and not check_winner(brett, current):  # game over?
    # play
    current = "X" if (current == None or current == "O") else "O"
    row, col = map(int, input("Enter the move for " + current + ": ").split(","))
    while not verify_entry(brett, row, col):
        print("Wrong entry. Think again!")
        row, col = map(int, input("Enter the move for " + current + ": ").split(","))
    update_board(brett, row, col, current)
    print_board(brett)  # prints the current board
    moves = moves + 1

if check_winner(brett, current):
    print(current + " WON!")
else:
    print("Nobody won!")
