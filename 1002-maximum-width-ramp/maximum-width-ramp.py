class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        rightMax = [0]*n
        rightMax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], nums[i])
        
        left, right = 0,0 
        maxWidth = 0
        while right <n:
            while left < right and nums[left] > rightMax[right]:
                left+=1
            maxWidth = max(maxWidth, right-left)
            right+=1
        return maxWidth