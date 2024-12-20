class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        return self.dfs(n, k, target, memo)

    def dfs(self, n, k, target, memo):
        if n==0:
            return 1 if target==0 else 0
        if (n, target) not in memo:
            ways = 0
            for i in range(1,k+1):
                ways+=self.dfs(n-1, k, target-i, memo)
            memo[(n, target)] = ways%1000000007
        return memo[(n, target)]