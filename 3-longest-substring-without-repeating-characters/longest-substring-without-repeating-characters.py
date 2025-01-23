class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start, end = 0,0
        maxLen = 0
        while end<len(s):
            while start<end and s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            maxLen = max(maxLen, end-start+1)
            end+=1
        return maxLen
