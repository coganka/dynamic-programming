# memoization
def gold_mine(mine):
    max_gold = 0
    lookup = {}
    for j in range(len(mine[0])):
        max_gold = max(max_gold, helper(mine, 0, j, lookup))
    return max_gold

def helper(mine, i, j, lookup):
    if (i,j) in lookup:
        return lookup[(i,j)]
    elif i == len(mine) or j == len(mine[0]) or j < 0:
        return 0
    else:
        lookup[(i,j)] = mine[i][j] + max(helper(mine, i+1, j, lookup), helper(mine, i+1, j-1, lookup), helper(mine, i+1, j+1, lookup))
        return lookup[(i,j)]
    
# tabulation
def tabu_gold(mine):
    n, m = len(mine), len(mine[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        dp[0][i] = mine[0][i]
    
    for i in range(1,n):
        for j in range(m):
            top_left = dp[i-1][j-1] if j-1 >= 0 else 0
            top_right = dp[i-1][j+1] if j+1 < m else 0
            top = dp[i-1][j]
            dp[i][j] = mine[i][j] + max(top, top_left, top_right)
    
    return max(dp[n-1])