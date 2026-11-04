# You are trying to make a checkerboard made up of X's and O's. You've implemented the function before in a different language but it just won't work. The function should create an n by n board of X's and O's.

# For example (Input --> Output)

# # n = 5 should give
# [['X', 'O', 'X', 'O', 'X'],
#  ['O', 'X', 'O', 'X', 'O'],
#  ['X', 'O', 'X', 'O', 'X'],
#  ['O', 'X', 'O', 'X', 'O'],
#  ['X', 'O', 'X', 'O', 'X']]

def make_checkered_board(n):
    board = [['X'] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            if (row+col)%2:
                board[row][col]="O"
    return board