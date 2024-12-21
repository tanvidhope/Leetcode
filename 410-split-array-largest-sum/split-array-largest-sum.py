class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        ans = left
        while (left <= right):
            mid = left + (right-left)//2
            subArrays = self.makeSubarrays(nums, k, mid)
            if subArrays > k:
                left = mid+1
            else:
                if subArrays == k:
                    ans = mid
                right = mid-1
        return ans

    def makeSubarrays(self, nums, k, mid):
        numPartitions = 1
        currSum = 0
        for num in nums:
            currSum+=num
            if currSum>mid:
                numPartitions+=1
                currSum = num
        return numPartitions
