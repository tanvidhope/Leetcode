class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # create a LCS
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i,c in enumerate(str1):
            for j,d in enumerate(str2):
                dp[i+1][j+1] = 1+ dp[i][j] if c == d else max(dp[i+1][j], dp[i][j+1])
        i,j, stack = m-1, n-1, []
        while i>=0 and j>=0:
            if str1[i] == str2[j]:
                stack.append(str1[i])
                i-=1
                j-=1
            elif dp[i+1][j] < dp[i][j+1]:
                stack.append(str1[i])
                i-=1
            else:
                stack.append(str2[j])
                j-=1
        return str1[:i+1] +str2[:j+1] + "".join(reversed(stack))