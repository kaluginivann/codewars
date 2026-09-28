# Am I A Passed Pawn?
# In chess, pawns are the weakest piece. But if they make it to the end of the board, they can promote to a queen.

# Pawns move forward in a straight line, and capture other pieces diagonally in front of them. A passed pawn is a pawn that has no enemy pawns in front of it which could block or capture it.

# You are trying to figure out if the white pawn is a passed pawn, whether or not it can make it to the 8th rank unimpeded.

# Note:
# In chess, rows are called ranks (1..8), and columns are called files (a..h).

# Examples
# Example #1:

# 8  . . . . . ↑ . .
# 7  p p p p . ↑ . p
# 6  . . . . . ↑ . .
# 5  . . . . . ↑ . .
# 4  . . . . . ↑ . .
# 3  . . . . . P . .
# 2  . . . . . . . .
# 1  . . . . . . . .
#    a b c d e f g h 
# The white pawn (P) on f3 is a passed pawn, because there is no black pawn (p) on the f-file (column) to block it, and no black pawns on the e or g files (columns) to capture it as it tries to move past (see the path marked by the arrows).

# Example #2:

# 8  . . ↑ . . . . .
# 7  p . ↑ . p . p p
# 6  . . ↑ . . p . .
# 5  . . P p . . . .
# 4  . p . . . . . .
# 3  . . . . . . . .
# 2  . . . . . . . .
# 1  . . . . . . . .
#    a b c d e f g h 
# The white pawn on c5 is a passed pawn. The black pawn on d5 cannot move backwards or horizontally, so there is no way to stop the white pawn reaching c8.

# Example #3:

# 8  . . . . . . . .
# 7  . . . . p . . .
# 6  . . . X . . . .
# 5  . . . ↑ . . . .
# 4  . . . ↑ . . . .
# 3  . . . P . . . .
# 2  . . . . . . . .
# 1  . . . . . . . .
#    a b c d e f g h 
# The white pawn on d3 is not a passed pawn. The black pawn on e7 will be able to capture it as it tries to move past.

# Input / Output:
# Input: You will be given a 2-dimensional array representing the 8x8 chess board from White's perspective. Each square will either have " " (nothing), "p" (a black pawn), or "P" (the white pawn). There will only be one white pawn.

# [
# [" "," "," "," "," "," "," "," "],  <-- 8th rank    ↑
# ["p","p"," "," "," ","p"," "," "],                  ↑
# [" "," ","p"," "," "," ","p"," "],                  ↑
# [" "," "," "," "," "," "," ","p"],                  ↑  white pawn moves
# [" "," "," "," "," "," "," "," "],                  ↑  towards 8th rank
# [" "," "," "," ","P"," "," "," "],                  ↑
# [" "," "," "," "," "," "," "," "],                  ↑
# [" "," "," "," "," "," "," "," "]   <-- 1st rank    ↑
# ]
#   ^                           ^
# a-file                      h-file
# Output: Either true or false, depending on whether or not the white pawn is a passed pawn.

# Good Luck! :)

def passed_pawn(board):
    white_row, white_col = -1, -1
    for r in range(8):
        for c in range(8):
            if board[r][c] == "P":
                white_row, white_col = r, c
                break
        if white_row != -1:
            break
    
    for r in range(white_row):
        for c in range(8):
            if board[r][c] == "p":
                if abs(c - white_col) <= 1:
                    return False
    
    return True