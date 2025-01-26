class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans =[]
        for word in words:
            dp = [False]*(len(word)+1)
            dp[0] = True
            for i in range(1,len(word)+1):
                for j in range((i==len(word) and 1 or 0), i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in wordSet
            if dp[-1] == True:
                ans.append(word)
        return ans
            