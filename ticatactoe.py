def create_board():
    """Prints an empty board. Provided for guidance, not necessary in this program.
    """
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")


def print_board(board):
    """Prints current board

    Parameters:
    board (list): a 3x3 list with board's positions
   """


def check_winner(board: list, current_player):
    """Returns True if the current player won, False otherwise

    Parameters:
    board (list): a 3x3 list with board's positions
    current_player(None or str): None for no player yet, "X" or "O"

    """


def update_board(board, row, col, current_player):
    """Update list with position taken on last move

    Parameters:
    board (list): a 3x3 list with board's position
    row(int): The row [0-2]
    col(int): The column [0-2]
    current_player(str): "X" or "O"

    """


def verify_entry(board, row, col):
    """
    Return: True if row.col is empty and inside the interval

    Parameters:
    board (list): a 3x3 list with board's positions
    row(int): The row [0-2]
    col(int): The column [0-2]    
   """


board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_board(board)  # prints an empty board
current = None
moves = 0
while moves < 9 and not check_winner(board, current):  # game over?
    # play
    current = "X" if (current == None or current == "O") else "O"
    row, col = map(int, input("Enter the move for " + current + ": ").split(","))
    while not verify_entry(board, row, col):
        print("Wrong entry. Think again!")
        row, col = map(int, input("Enter the move for " + current + ": ").split(","))
    update_board(board, row, col, current)
    print_board(board)  # prints the current board
    moves = moves + 1

if moves < 9:
    print(current + " WON!")
