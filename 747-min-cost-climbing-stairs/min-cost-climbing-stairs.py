class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1]*n
        return min(self.dp(cost, 0, memo), self.dp(cost, 1, memo))

    def dp(self, cost, i, memo):
        if i>=len(cost):
            return 0
        if memo[i]==-1:
            memo[i] = cost[i]+min(self.dp(cost, i+1, memo), self.dp(cost, i+2, memo))
        return memo[i]