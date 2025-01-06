def max_square(matrix):
    n,m = len(matrix), len(matrix[0])
    lookup = {}
    max_size = 0
    for i in range(n):
        for j in range(m):
            max_size = max(max_size, helper(matrix, i, j, lookup))
    return max_size ** 2

def helper(matrix, i, j, lookup):
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i < 0 or j < 0 or matrix[i][j] == 0:
        return 0
    if i == 0 or j == 0:
        lookup[(i, j)] = matrix[i][j]
    else:
        lookup[(i,j)] = 1 + min(helper(matrix, i-1, j, lookup), helper(matrix, i, j-1, lookup), helper(matrix, i-1, j-1, lookup))
    return lookup[(i,j)]


# tabulation
def tabu_square(matrix):
    n, m = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = matrix[0][0]
    max_size = dp[0][0]

    for i in range(1, n):
        dp[i][0] = matrix[i][0]
        max_size = max(max_size, dp[i][0])
    for j in range(1, m):
        dp[0][j] = matrix[0][j]
        max_size = max(max_size, dp[0][j])
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = 0 if matrix[i][j] == 0 else 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            max_size = max(max_size, dp[i][j])

    return max_size ** 2



matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(max_square(matrix))