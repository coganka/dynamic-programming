def fibo(n, lookup=None):
    lookup = {} if lookup is None else lookup
    if n in lookup:
        return lookup[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    lookup[n] = fibo(n-1, lookup) + fibo(n-2, lookup)
    return lookup[n]
    
print(fibo(10))