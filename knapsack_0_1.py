def knapsack(values, weights, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (k, i) in lookup:
        return lookup[(k,i)]
    elif i == len(values):
        return 0
    elif weights[i] > k:
        lookup[(k,i)] = knapsack(values, weights, k, i+1, lookup)
        return lookup[(k,i)]
    else:
        lookup[(k,i)] = max(values[i] + knapsack(values, weights, k-weights[i], i+1, lookup), knapsack(values, weights, k, i+1, lookup))
        return lookup[(k,i)]
    
values = [20,30,15,25,10]
weights = [6,13,5,10,3]
print(knapsack(values, weights, 20))