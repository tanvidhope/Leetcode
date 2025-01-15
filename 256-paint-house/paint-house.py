class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0]*n for i in range(3)]
        dp[0][0] = costs[0][0]
        dp[1][0] = costs[0][1]
        dp[2][0] = costs[0][2]

        for i in range(1,n):
            dp[0][i] = costs[i][0] + min(dp[1][i-1], dp[2][i-1])
            dp[1][i] = costs[i][1] + min(dp[0][i-1], dp[2][i-1])
            dp[2][i] = costs[i][2] + min(dp[1][i-1], dp[0][i-1])
        return min(dp[0][-1], dp[1][-1], dp[2][-1])