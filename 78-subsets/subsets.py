class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # all possible subsets
        ans = []
        self.backtrack(nums, 0, [], ans)
        return ans

    def backtrack(self, nums, i, curr, ans):
        if i>=len(nums):
            ans.append(curr.copy())
            return
        curr.append(nums[i])
        self.backtrack(nums, i+1, curr, ans)
        curr.pop()
        self.backtrack(nums, i+1, curr, ans)