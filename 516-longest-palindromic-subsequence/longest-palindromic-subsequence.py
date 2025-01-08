class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        t = s[::-1]
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i][j] = 1+dp[i-1][j-1] if i>0 and j>0 else 1
                else:
                    top = dp[i-1][j] if i>0 else 0
                    left = dp[i][j-1] if j>0 else 0
                    dp[i][j] = max(top, left)
        return dp[n-1][n-1]