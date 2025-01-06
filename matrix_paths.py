def paths(matrix, i=0, j=0, lookup=None):
    n, m = len(matrix), len(matrix[0])
    lookup = {} if lookup is None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i == n or j == m or matrix[i][j] == 1:
        return 0
    elif i == n-1 and j == m-1:
        return 1
    else:
        lookup[(i,j)] = paths(matrix, i, j+1, lookup) + paths(matrix, i+1, j, lookup)
        return lookup[(i,j)]
    
# tabulation
def tabu_paths(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1 if matrix[0][0] == 0 else 0

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] if matrix[0][j] == 0 else 0
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] if matrix[i][0] == 0 else 0
    
    for i in range(n):
        for j in range(m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] if matrix[i][j] == 0 else 0
    
    return dp[n-1][m-1]