class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0]*len(values)
        maxVal = 0
        dp[0]= values[0]
        for i in range(1,len(values)):
            maxVal = max(maxVal, dp[i-1]+values[i]-i)
            dp[i] = max(dp[i-1], values[i]+i)
        return maxVal