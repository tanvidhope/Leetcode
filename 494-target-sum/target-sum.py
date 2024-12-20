class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.findWays(nums, 0, target, memo)

    def findWays(self, nums, i, target, memo):
        if i>=len(nums):
            return 1 if target==0 else 0
        if (i, target) not in memo:
            memo[(i, target)] = self.findWays(nums, i+1, target-nums[i], memo) + self.findWays(nums, i+1, target+nums[i], memo)
        return memo[(i,target)]