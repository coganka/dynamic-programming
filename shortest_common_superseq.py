def scs(s1, s2, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    # if one of them at last index return remaining of other (supersequence)
    if i == len(s1):
        return len(s2) - j
    elif j == len(s2):
        return len(s1) - i
    # if same chars increase count and move on
    elif s1[i] == s2[j]:
        lookup[(i,j)] = 1 + scs(s1, s2, i+1, j+1, lookup)
        return lookup[(i,j)]
    # move i or move j, traverse through and get min
    lookup[(i,j)] = 1 + min(scs(s1,s2,i+1,j,lookup), scs(s1,s2,i,j+1,lookup))
    return lookup[(i,j)]

s1 = "abcfg"
s2 = "akj"
print(scs(s1,s2))