# Overbruk av funksjoner
#################################################################################
def check_winner(board, P):

    if ((board[0][0] == P and board[1][0] == P and board[2][0] == P or
        (board[0][1] == P and board[1][1] == P and board[2][1] == P or
        (board[0][2] == P and board[1][2] == P and board[2][2] == P or
#################################################################################
print(str(board[0][0]), "|",str(board[0][1]), "|", str(board[0][2]))
#################################################################################
print(board[0][0], "|", board[0][1], "|", board[0][2])
#################################################################################

# Returning bool is not a boolean value
return bool 

bool <class 'bool'> # <---- Type / Objekt

True == 1 # <---- Truth value
False == 0 # <---- Truth value

bool == True # False
#################################################################################

# Delvis sjekk av interval
def verify_entry():
    if row >= 0 and row < 3:
        return True

[-1] == Siste posisjon i listen

[1,2,3,4,5,6,7,8][-1] ==  8

#################################################################################

# Utilgjengelig kode. ref: "utilgjengelig_kode.py"
if board[row][col] != "1":
    return False
else:
    return True
if (
    row == board[0]
    or board[1]
    or board[2]
    and col == board[0]
    or board[1]
    or board[2]
):
    return True
else:
    return False
#################################################################################

# Feil bruk av AND eller OR
if (
    (row == board[0]
    or row == board[1]
    or row == board[2])
    and (col == board[0]
    or col ==  board[1]
    or col == board[2])
):

row == board[0]
    or board[1]
    or board[2]

(row == board[0]
    or row == board[1]
    or row == board[2])
and
(col == board[0]
    or col ==  board[1]
    or col == board[2])

row == (board[0] or board[1])

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

1 == (1 or 2)

#################################################################################

# Feil bruk av length

if len(board[row][col]) > 1:
    return False
else:
    return True

board = [["X", " ", "O"], [" ", "X", " "], ["O", " ", " "]]

#################################################################################

# Feil print board

def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])


['X', ' ', 'O']
[' ', 'X', ' ']
['O', ' ', ' ']

def create_board():
    """Prints an empty board. Provided for guidance, not necessary in this program.
    """
    print(" | | ")
    print("-+-+-")
    print(" | | ")
    print("-+-+-")
    print(" | | ")

Print(board[0][1]) # Riktig måte å hente ut noe ifra matrisen

