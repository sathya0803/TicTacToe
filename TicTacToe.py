#creating the list to hold the values of 9 boxes. Initially all are " "

l=["-"]*9

#game_still_going is declared as global . It is True until a player wins or match ties

game_still_going=True

#winner takes value True if a player wins else it'll remain tie since it'll be a tie

winner= None

#current_player variable is used to switch players and initialized to "X"

current_player="X"

#displaying the board


def display_board():
    print( l[0] + "|" + l[1] + "|" + l[2] )
    print( l[3] + "|" + l[4] + "|" + l[5] )
    print( l[6] + "|" + l[7] + "|" + l[8] )


def play():
    
    
    display_board()                    #when the game starts first we have to display the board
    
   while game_still_going:             #unless a player doesn't win or the game ties the loop runs
    
        handle_turn(current_player)    #used to alternate the turn of palyers
        check_gameover()               #used to check if gameover
        flip_players()                 #if the continues , the turn of players flips or changes

    if winner=="X" or winner=="O":
        print(winner+" WON......!!!!")
    elif winner==None:
        print("Tie")


def handle_turn(player):
    #To get user input, where the player have to insert X or O
    print(player+"Turn")
    x = ["1","2","3","4","5","6","7","8","9"]
    pos=input("enter the position:")
    valid=False
    while not valid:
        while pos not in x:
            pos = input( "Invalid Input... CHoose position from 1 to 9:" )

        pos = int( pos ) - 1
        if l[pos]=="-":
            valid = True
        else:
            print("You can't go there...!")
    l[pos] = player
    display_board()


def check_gameover():
    #if a player wins or match ties the game become over
    check_win()
    check_tie()


def check_win():
    #we can use the global variable in the function but inorder to alter we have declare it again in the function
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner=None
    return


def check_rows():
    global game_still_going
    row1 = l[0] == l[1] == l[2] != "-"
    row2 = l[3] == l[4] == l[5] != "-"
    row3 = l[6] == l[7] == l[8] != "-"
    #if any of the rows are equal then it is a win and gamestillgoing set as false
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return l[0]
    elif row2:
        return l[3]
    elif row3:
        return l[6]
    return


def check_columns():
    global game_still_going
    col1 = l[0] == l[3] == l[6] != "-"
    col2 = l[1] == l[4] == l[7] != "-"
    col3 = l[2] == l[5] == l[8] != "-"
    #if any of the col are equal then it is a win and gamestillgoing set as false
    if col1 or col2 or col3:
        game_still_going=False
    if col1:
        return l[0]
    elif col2:
        return l[1]
    elif col3:
        return l[2]
    return


def check_diagonals():
    global game_still_going
    diag1 = l[0] == l[4] == l[8] != "-"
    diag2 = l[2] == l[4] == l[6] != "-"
    #if any of the diagonals are equal then it is a win and gamestillgoing set as false
    if diag1 or diag2:
        game_still_going=False
    if diag1:
        return l[0]
    elif diag2:
        return l[2]
    return


def check_tie():
    global game_still_going
    if "-" not in l:
        game_still_going=False
    return


def flip_players():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return

play()
