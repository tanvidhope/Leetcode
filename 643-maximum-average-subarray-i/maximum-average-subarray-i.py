class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # prefix sum
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1]+nums[i]
        maxVal = prefix[k-1]/k
        for i in range(n-k):
            sum = prefix[i+k]-prefix[i]
            avg = sum/k
            maxVal = max(maxVal, avg)
        return maxVal