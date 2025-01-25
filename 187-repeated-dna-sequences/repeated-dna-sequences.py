class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hset = set()
        ans = set()
        for i in range(len(s)):
            if (i+9)<len(s):
                if s[i:i+10] in hset:
                    ans.add(s[i:i+10])
                else:
                    hset.add(s[i:i+10])
        return list(ans)