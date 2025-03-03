def longestSubstring(s,t):
    m,n = len(s),len(t)
    dp = [[0]*(n+1) for _ in range(m+1)]

    # Fill The DP Table
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    # Reconstruct The Subsequence From The DP Table
    i,j = m,n
    sub = []
    while i>0 and j>0:
        if s[j-1] == t[j-1]:
            sub.append(s[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1

    return ''.join(reversed(sub))


longestSubstring("asdgasdasfdjfdas","asdz")