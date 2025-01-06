def coin_change(num, coins):
    dp = [float("inf")] * (num+1)
    dp[0] = 0
    for i in range(1, num+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1+dp[i-coin])
    return -1 if dp[num] == float("inf") else dp[num]