# Question: find the shortest path value in 2d matrix, you can either move right or down.
def shortest_path(grid, i=0, j=0, lookup=None):
    n,m = len(grid), len(grid[0])
    lookup = {} if lookup is None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    # if out of bounds or its a wall return super high so it wont get selected in min()
    if i < 0 or i == n or j < 0 or j == m or grid[i][j] == -1:
        return float("inf")
    # got to the destination dont search just save and return grid value 
    elif i == n-1 and j == m-1:
        lookup[(i,j)] = grid[i][j]
        return lookup[(i,j)]
    # traverse down and right
    down = shortest_path(grid, i+1, j, lookup)
    right = shortest_path(grid, i, j+1, lookup)
    # get the min of possible ways and add current value
    lookup[(i,j)] = grid[i][j] + min(down, right)

    return lookup[(i,j)]