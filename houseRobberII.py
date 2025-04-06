def helper(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    dp = [0] * len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0],houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(houses[i]+dp[i-2],dp[i-1])
    return dp[-1]

def rob(houses):
    if len(houses) == 1:
        return houses[0]
    return max(helper(houses[1:]),helper(houses[:-1]))