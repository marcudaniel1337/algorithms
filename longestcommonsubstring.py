def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return ""
    
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # trace back
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))


def lcs_length_only(s1, s2):
    if not s1 or not s2:
        return 0
    
    m, n = len(s1), len(s2)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, prev
    
    return prev[n]


# examples
s1 = "ABCDGH"
s2 = "AEDFHR"
print(f"'{s1}' and '{s2}': '{longest_common_subsequence(s1, s2)}'")

s1 = "AGGTAB" 
s2 = "GXTXAYB"
print(f"'{s1}' and '{s2}': '{longest_common_subsequence(s1, s2)}'")

print(f"Length only: {lcs_length_only('PROGRAMMING', 'DEBUGGING')}")
