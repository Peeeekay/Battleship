#-------------------------------------------------------------------------------
from random import randint
#n is Number of players want to play this game.
# 5 ships
# Person who guesses first wins the game

try:
    n=int(raw_input("Number of Players:" ))
except KeyboardInterrupt: #check whether the user clicked cancel
    print "Oops!  That was no valid number."
    n=0
except ValueError: #check whether user did not enter any value
    print "No Value Entered"
    n=0


boards=[] #number of boards req
ships=[]  #list containing all the ships
tfs=[]    #list containing true and false
for k in range(n):
    ships.append(5)
def random_row(board):              #x co-ordinate of the ship
    row= randint(0, len(board) - 1)
    return row
def random_col(board):              #y co-ordinate of the ship
    col= randint(0, len(board[0]) - 1)
    return col
for i in range(0,n):
    board = []
    tf=[]
    for x in range(10):
        board.append(["O"] * 10)
        tf.append(["False"]*10)
    def print_board(board):
        for row in board:
            print " ".join(row)
    for k in range(5):
        r=random_row(board)
        c=random_col(board)
        ship_row=board[r]
        ship_col=board[c]
        tf[r][c]="True"             #Postition of ships is true , everything other box is false.

    tfs.append(tf)
    boards.append(board)


i=0
p=1
def check(guess_row, guess_col,TF, Board, Ship):
    if guess_row==100 or guess_col ==100:
        return "q"
    elif  guess_row > 9 or guess_col > 9:
            return "r"
    elif TF[guess_row][guess_col] == "True":
        return "W"

    else:
        if(Board[guess_row][guess_col] == "X")or Board[guess_row][guess_col]=="B":
            return "a"
        else:
            return "L"
if n!=0:
    print print_board(board)
test=1;
while p==1:
    if n==0:
        break;
    print "Player %s turn"%(i+1)
    print "Player %s : You have %s left"%(i+1,ships[i])

    try:
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    except KeyboardInterrupt:
        print "You clicked Cancel, My friend!"
        test=0;
    except ValueError:
        print "No Value Entered"
        test=0;

    if test==0:
        break;
    d=check(guess_row, guess_col,tfs[i],boards[i],ships[i])

    if d=="W":
        print "Congratulations! You sunk my battleship!"
        ships[i]=ships[i]-1
        k=k+1
        tfs[i][guess_row][guess_col]="False"
        boards[i][guess_row][guess_col]="B"
        #His turn Again
        if ships[i]==0:
            print "You win"
            p=3

    elif d=="r":
        print "Oops, that's not even in the ocean."
        i=i

    elif d=="q":
        print "Game ended"
        p=2
    elif d=="a":
        print "You guessed that one already."
        #His turn again
    elif d=="L":
        print "You missed my battleship!"
        boards[i][guess_row][guess_col] = "X"
        #His turn again.
    print "Player %s Board: "%(i+1)

    print print_board(boards[i])

    #Alternate turns

    if d=="L":
        if i==n-1:
            i=0
        else:
            i=i+1