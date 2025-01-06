# you can climb either 1,2,3 steps at a time
# tabulation
def climb_stairs(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(1,4):
            if i-j >= 0:
                dp[i] += dp[i-j]
    return dp[-1]

def memo_stairs(n, lookup=None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n < 0:
        return 0
    elif n == 0:
        return 1    
    lookup[n] = memo_stairs(n-1, lookup) + memo_stairs(n-2, lookup) + memo_stairs(n-3, lookup)
    return lookup[n]

print(memo_stairs(4))