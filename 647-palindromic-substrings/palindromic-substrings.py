class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1):
            count+=self.findCount(s, i, i)
            count+=self.findCount(s, i, i+1)
        return count+1
    
    def findCount(self, s, i,j):
        count = 0
        while i>=0 and j<len(s) and s[i] == s[j]:
            i-=1
            j+=1
            count+=1
        return count