class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # difference array
        if len(nums) == 1:
            return 1
        maxValue = max(nums)
        count = [0]*(maxValue+1)
        for num in nums:
            count[max(num-k, 0)]+=1
            if num+k+1 <= maxValue:
                count[num+k+1]-=1
        maxBeauty = 0
        currSum = 0
        for val in count:
            currSum+=val
            maxBeauty= max(maxBeauty, currSum)
        return maxBeauty