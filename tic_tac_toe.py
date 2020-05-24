# tic tac toe game

# -----Global variables------

# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
# if game still going
game_still_going = True
# who won or tie
winner = None
# whos turn is it
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play game
def play_game():

    # display initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip between players
        flip_player()

    # we have a winner
    if winner == "X" or winner == "O":
        print(winner + " won!!")
    # there is a tie
    elif winner == None:
        print("It's a tie!")


# handle a single turn
def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1 to 9: ")

    # verify if position it's free
    valid = False
    while not valid:
        # only accept number from 1 to 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()


# check if the game has ended
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# check if someone won
def check_for_winner():
    # setup global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# check rows
def check_rows():
    # set global variables
    global game_still_going
    # check if any of the rows have the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any of the rows is a match flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]  
    return


# check columns
def check_columns():
    # set global variables
    global game_still_going
    # check if any of the columns have the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any of the columns is a match flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2] 
    return


# check diagonals
def check_diagonals():
    # set global variables
    global game_still_going
    # check if any of the columns have the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any of the columns is a match flag that there is a win
    if diagonal_2 or diagonal_2:
        game_still_going = False
    # return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# check if tie
def check_if_tie():
    # set global variable
    global game_still_going
    # if there are no more -
    if "-" not in board:
        game_still_going = False
    return

# flip between players
def flip_player():
    # set global variables
    global  current_player
    # change player from X to O
    if current_player == "X":
        current_player = "O"
    # change player from O to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()

