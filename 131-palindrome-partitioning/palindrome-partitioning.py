class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.helper(s, [], 0, ans)
        return ans

    def helper(self, s, current, start, ans):
        if start>=len(s):
            ans.append(current.copy())

        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                current.append(s[start:end+1])
                self.helper(s, current, end+1, ans)
                current.pop()
        
    def isPalindrome(self, s, start, end):
        while (start<=end):
            if (s[start] == s[end]):
                start+=1
                end-=1
            else:
                return False
        return True