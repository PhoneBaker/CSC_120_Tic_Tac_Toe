tictactoe_board = ["*", "*", "*",
                   "*", "*", "*",
                   "*", "*", "*"]
game_in_play = True
winner = None
player1 = "X"
player2 = "O"


def display_tictactoe_board():
    print(tictactoe_board[0] + "|" + tictactoe_board[1] + "|" + tictactoe_board[2])
    print(tictactoe_board[3] + "|" + tictactoe_board[4] + "|" + tictactoe_board[5])
    print(tictactoe_board[6] + "|" + tictactoe_board[7] + "|" + tictactoe_board[8])


    # start playing
def play_game():
    display_tictactoe_board()
    player = "X"
    while game_in_play:
        take_turn(player)
        if player == "X":
            player = "O"
        else:
            player = "X"
        check_win()
        check_tie()

    if winner == "X" or winner == "O":
        print(winner + " is the winner!!")
    else:
        print("No winner: Tie.")


# handle players taking turn
def take_turn(player):
    valid = False

    while not valid:
        placement = input(f"It's {player}'s turn. Choose a spot for your X. Choose a spot from 0-8: ")
        placement = int(placement)
        if tictactoe_board[placement] != "*":
            print("Oops, this spot is occupied. Please choose another spot.")
        else:
            tictactoe_board[placement] = player
            display_tictactoe_board()
            break


# check for winner
def check_win():
    global winner
    row_win = check_rows()
    col_win = check_col()
    diagonal_win = check_diag()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_rows():
    global game_in_play
    row1 = tictactoe_board[0] == tictactoe_board[1] == tictactoe_board[2] != "*"
    row2 = tictactoe_board[3] == tictactoe_board[4] == tictactoe_board[5] != "*"
    row3 = tictactoe_board[6] == tictactoe_board[7] == tictactoe_board[8] != "*"

    if row1 or row2 or row3:
        game_in_play = False
        # return winner
    if row1:
        return tictactoe_board[0]
    elif row2:
        return tictactoe_board[3]
    elif row3:
        return tictactoe_board[6]
    else:
        return None


def check_col():
    global game_in_play
    col1 = tictactoe_board[0] == tictactoe_board[3] == tictactoe_board[6] != "*"
    col2 = tictactoe_board[1] == tictactoe_board[4] == tictactoe_board[7] != "*"
    col3 = tictactoe_board[2] == tictactoe_board[5] == tictactoe_board[8] != "*"

    if col1 or col2 or col3:
        game_in_play = False
        # return winner
    if col1:
        return tictactoe_board[0]
    elif col2:
        return tictactoe_board[1]
    elif col3:
        return tictactoe_board[2]
    else:
        return None


def check_diag():
    global game_in_play
    diag1 = tictactoe_board[2] == tictactoe_board[4] == tictactoe_board[6] != "*"
    diag2 = tictactoe_board[0] == tictactoe_board[4] == tictactoe_board[8] != "*"

    if diag1 or diag2:
        game_in_play = False
        # return winner
    if diag1:
        return tictactoe_board[2]
    elif diag2:
        return tictactoe_board[0]
    else:
        return None


def check_tie():
    global game_in_play
    if "*" not in tictactoe_board:
        game_in_play = False
        return True
    else:
        return False


play_game()