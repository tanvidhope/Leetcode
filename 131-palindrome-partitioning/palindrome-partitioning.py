class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.canPartition(s, 0, [], ans)
        return ans

    def canPartition(self, s, i, curr, ans):
        if i>=len(s):
            ans.append(curr.copy())
            return
        for j in range(i,len(s)):
            if self.isPalindrome(s, i, j):
                curr.append(s[i:j+1])
                self.canPartition(s, j+1, curr, ans)
                curr.pop()
        return
    
    def isPalindrome(self, s, start, end):
        while start<=end and s[start]==s[end]:
            start+=1
            end-=1
        return True if start>=end else False