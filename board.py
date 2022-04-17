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

