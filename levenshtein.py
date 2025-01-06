def levenshtein(word1, word2, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i,j) in lookup:
        return lookup[(i,j)]
    if i == len(word1):
        return len(word2)-i
    elif j == len(word2):
        return len(word1)-j
    elif word1[i] == word2[j]:
        lookup[(i,j)] = levenshtein(word1, word2, i+1, j+1, lookup)
        return lookup[(i,j)]
    lookup[(i,j)] = 1 + min(levenshtein(word1,word2,i,j+1,lookup), levenshtein(word1, word2, i+1, j, lookup), levenshtein(word1, word2, i+1, j+1, lookup))
    return lookup[(i,j)]

# tabulation
def tabu_levo(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for j in range(1, m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        dp[i][0] = i
    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
    return dp[n][m]