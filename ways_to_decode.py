def ways(s, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]
    if i == len(s):
        return 1
    elif s[i] == "0":
        return 0
    elif i+1 < len(s) and "10" <= s[i] + s[i+1] <= "26":
        lookup[i] = ways(s, i+1, lookup) + ways(s, i+2, lookup)
        return lookup[i]
    lookup[i] = ways(s, i+1, lookup)
    return lookup[i]

s = "123"
print(ways(s))