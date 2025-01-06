# sum(ways(n-for jump in jumps))
def ways(jumps, n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for jump in jumps:
            if i-jump >= 0:
                dp[i] += dp[i-jump]
    return dp[n]

jumps = [2,4,5,8]
print(ways(jumps, 10))