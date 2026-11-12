# Write a function that returns the center of a 2-dim array.

# It should return nil / None / null / Nothing (etc., use your language's equivalent for an empty value) if there is no single center element.

# You can assume all inputs will be rectangular matrices in array form. ex: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def center(mat):
    if not mat or not mat[0]:
        return None
    
    rows = len(mat)
    cols = len(mat[0])
    
    if rows % 2 == 0 or cols % 2 == 0:
        return None
    
    return mat[rows // 2][cols // 2]