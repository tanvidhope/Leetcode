class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        leftmost = 0
        for i in range(len(s)):
            if s[i] < s[leftmost]:
                leftmost = i
            freq[s[i]]-=1
            if freq[s[i]] ==0:
                break
        # remove further occurences of s as well
        return s[leftmost] + self.removeDuplicateLetters(s[leftmost:].replace(s[leftmost], "")) if s else ""