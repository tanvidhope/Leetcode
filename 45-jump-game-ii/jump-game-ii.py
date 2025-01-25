class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i, min(n,i+nums[i]+1)):
                dp[i] = min(dp[i], dp[j]+1)
        return dp[0]

