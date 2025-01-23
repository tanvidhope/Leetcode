class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(n, 0, 0, "", ans)
        return ans

    def backtrack(self, n, open, closed, curr, ans):
        if open == n and closed == open:
            ans.append(curr)
            return
        if open<n:
            curr+="("
            self.backtrack(n, open+1, closed, curr, ans)
            curr = curr[:-1]
        if closed<open:
            curr+=')'
            self.backtrack(n, open, closed+1, curr, ans)
            curr=curr[:-1]