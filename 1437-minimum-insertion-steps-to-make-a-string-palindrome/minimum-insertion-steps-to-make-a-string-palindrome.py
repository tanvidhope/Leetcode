class Solution:
    def minInsertions(self, s: str) -> int:
        # start from the end and see if adding either left char or right char gives least ans
        # dp
        # basically find the longest common subsequence between s and reversed(s)
        # n- lcs(s, reversed(s)) is the number of characters you need to insert to make it palindromic.
    
        n = len(s)
        dp = [[0]*(n+1) for i in range(n+1)]
        for i in range(n):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j]+1 if s[i] == s[n-1-j] else max(dp[i][j+1], dp[i+1][j])
        return n-dp[n][n]