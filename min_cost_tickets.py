def ticket_cost(train_days, costs, n, day=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if day in lookup:
        return lookup[day]
    if day >= n:
        return 0
    elif day not in train_days:
        lookup[day] = ticket_cost(train_days, costs, n, day+1, lookup)
        return lookup[day]
    lookup[day] = min(costs[0] + ticket_cost(train_days, costs, n, day+1, lookup), 
                      costs[1] + ticket_cost(train_days, costs, n, day+7, lookup),
                      costs[2] + ticket_cost(train_days, costs, n, day+30, lookup))
    return lookup[day]

def tabu_cost(train_days, costs, n):
    dp = [0] * n
    for i in range(n):
        if i not in train_days:
            dp[i] = dp[i-1] if i-1 >= 0 else 0
        else:
            day_cost = costs[0] + (dp[i-1] if i-1 >= 0 else 0)
            week_cost = costs[1] + (dp[i-7] if i-7 >= 0 else 0)
            month_cost = costs[2] + (dp[i-30] if i-30 >= 0 else 0)
            dp[i] = min(day_cost, week_cost, month_cost)
    return dp[n-1]


def calcost(days, costs, trains):
    dp = [0] * len(days)
    for i in range(len(days)):
        if i not in days:
            dp[i] = dp[i-1] if i-1 >= 0 else 0
        else:
            cost = float("inf")
            for j in range(len(trains)):
                cost = min(cost, costs[j] + (dp[i-trains[j]] if i-trains[j] >= 0 else 0))
            dp[i] = cost
    return dp[-1]