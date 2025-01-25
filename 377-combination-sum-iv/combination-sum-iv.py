class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo ={}
        return self.makeCombination(nums, target, memo)

    def makeCombination(self, nums, target, memo):
        if target<0:
            return 0
        if target ==0 :
            return 1
        if target not in memo:
            ans = 0
            for num in nums:
                ans+=self.makeCombination(nums, target-num, memo)
            memo[target] = ans
        return memo[target]