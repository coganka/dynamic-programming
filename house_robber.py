def house_robber(houses):
    if len(houses) == 1:
        return houses[0]
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1]) # max of first house or second house, easier traverse
    for i in range(2,len(houses)):
        # max of 2 non adjacents or one before
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])
    return dp[-1]