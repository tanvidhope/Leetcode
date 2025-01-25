class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wordSet:
                    dp[i+1] = True
        return dp[n]