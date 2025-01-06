def rod_cutting(n, prices, lookup=None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n == 0:
        lookup[n] = 0
        return 0
    max_price = 0
    for len in range(1, n+1):
        if n-len >= 0:
            max_price = max(max_price, prices[len] + rod_cutting(n-len, prices, lookup))
    lookup[n] = max_price
    return lookup[n]

# tabulation
def tabu_rod(n, prices):
    dp = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        for len in range(1,i+1):
            dp[i] = max(dp[i], prices[len]+ dp[i-len])
    return dp[n]