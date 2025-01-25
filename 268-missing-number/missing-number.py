class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans1, ans2 = 0,0
        for num in nums:
            ans1^=num
    
        for i in range(len(nums)+1):
            ans2=ans2^i
        return ans1^ans2