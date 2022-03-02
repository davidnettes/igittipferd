2/# Project Inititalized: 18/02/2022 
# 21:31 

# Beginning of the tictactoe.py project..

# FOR REFERENCE: Number Grid and Empty game board:

# - | - | -
# - | - | -       
# - | - | -

# 1 | 2 | 3 
# 4 | 5 | 6 
# 7 | 8 | 9

##############################################################################
# INTRO TO THE GAME
##############################################################################

import random

print("""\n
Let's play TicTacToe!\n
These are the game board and the corresponding number tiles.\n
- | - | -       1 | 2 | 3 
- | - | -       4 | 5 | 6 
- | - | -       7 | 8 | 9
\nRemember the numbers!\n""")

def create_board():
    player = 0
    x = 0
    board_update = {}
    board_start = {1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
    while x == 0:
        if player % 2 == 0:
            print("Player X, its your turn: ")
            board_update[int(input('Enter valid number: '))] = "X"
        else:
            print("Player O, its your turn: ")
            board_update[int(input('Enter valid number: '))] = "O"
        for i in board_update:
            board_start[i] = board_update[i]
        player += 1

        print(f"""
        {board_start[1]} | {board_start[2]} | {board_start[3]}
        {board_start[4]} | {board_start[5]} | {board_start[6]}
        {board_start[7]} | {board_start[8]} | {board_start[9]}
            """)

create_board()