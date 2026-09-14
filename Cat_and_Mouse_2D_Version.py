# You will be given a string (map) featuring a cat "C" and a mouse "m". The rest of the string will be made up of dots (".") The cat can move the given number of moves up, down, left or right, but not diagonally.

# You need to find out if the cat can catch the mouse from it's current position and return "Caught!" or "Escaped!" respectively.

# Finally, if one of two animals are not present, return "boring without two animals".

# Examples
# moves = 5

# map =
# ..C......
# .........
# ....m....

# returns "Caught!" because the cat can catch the mouse in 4 moves
# moves = 5

# map =
# .C.......
# .........
# ......m..

# returns "Escaped!" because the cat cannot catch the mouse in  5 moves

def cat_mouse(map_, moves):
    lines = map_.split('\n')
    
    cat_pos = None
    mouse_pos = None
    
    for row_idx, line in enumerate(lines):
        for col_idx, char in enumerate(line):
            if char == 'C':
                cat_pos = (row_idx, col_idx)
            elif char == 'm':
                mouse_pos = (row_idx, col_idx)
    
    if cat_pos is None or mouse_pos is None:
        return "boring without two animals"
    
    distance = abs(cat_pos[0] - mouse_pos[0]) + abs(cat_pos[1] - mouse_pos[1])
    
    if distance <= moves:
        return "Caught!"
    else:
        return "Escaped!"