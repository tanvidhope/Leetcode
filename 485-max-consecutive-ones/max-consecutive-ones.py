class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        currVal = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                currVal+=1
            else:
                maxVal = max(maxVal, currVal)
                currVal = 0
        return max(currVal, maxVal)