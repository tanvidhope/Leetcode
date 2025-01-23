class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum, minLen, start, end = 0,float('inf'),0,0
        while end<len(nums):
            currSum+=nums[end]
            end+=1
            while(start<=end and currSum>=target):
                minLen = min(minLen, end-start)
                currSum-=nums[start]
                start+=1
        return minLen if minLen!=float('inf') else 0