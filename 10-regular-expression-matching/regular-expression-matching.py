class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s), len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2] and True
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] # matches 0 occurences
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j]= dp[i][j] or dp[i-1][j]
                elif p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]
