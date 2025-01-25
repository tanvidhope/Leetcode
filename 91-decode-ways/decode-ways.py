class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        return self.decode(s, 0, memo)
        
    def decode(self, s, curr, memo):
        if curr>=len(s):
            return 1
        if s[curr] == "0":
            return 0
        if curr not in memo:
            count = 0
            count+=self.decode(s, curr+1, memo)
            if int(s[curr:curr+2]) >=10 and int(s[curr:curr+2])<=26:
                count+=self.decode(s, curr+2, memo)
            memo[curr] = count
        return memo[curr]