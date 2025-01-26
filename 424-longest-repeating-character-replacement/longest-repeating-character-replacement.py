class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end, maxChar = 0, 0, 0
        maxLen = 0
        map = defaultdict(int)
        for end in range(len(s)):
            map[s[end]]+=1
            if map[s[end]] > maxChar:
                maxChar = map[s[end]]
            if end-start+1-maxChar > k:
                map[s[start]]-=1
                start+=1
            maxLen = max(maxLen, end-start+1)
        return maxLen