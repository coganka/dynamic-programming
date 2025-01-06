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