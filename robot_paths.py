# input is row X col, you can only go down or right, find unique paths
def unique_ways(m, n):
    # they can accessible by default so at least 1 path
    dp = [[1 for _ in range(n)] for _ in range(m)] 
    # first row and first col have only one path (you cant move up or left) so skip it
    for row in range(1, m):
        for col in range(1, n):
            # bottom up approach, sum of possible ways to get to top and left adjacents
            dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[-1][-1] # bottom right

print(unique_ways(3,7))