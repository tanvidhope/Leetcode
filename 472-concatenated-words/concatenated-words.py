class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans = []
        for word in words:
            if self.canFormWord(wordSet, word):
                ans.append(word)
        return ans
    
    def canFormWord(self, words, word):
        n = len(word)
        words.remove(word)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1):
                if dp[j] and word[j:i+1] in words:
                    dp[i+1] = True
        words.add(word)
        return dp[n]