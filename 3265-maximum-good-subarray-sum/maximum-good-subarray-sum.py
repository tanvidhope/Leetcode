class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        currentSum = 0
        maxSum = float('-inf')
        for num in nums:
            if num-k in prefixSum:
                minValue = prefixSum[num-k]
                maxSum = max(maxSum, currentSum+num-minValue)
            if num+k in prefixSum:
                minValue = prefixSum[num+k]
                maxSum = max(maxSum, currentSum+num-minValue)
            currPrefixSum = prefixSum[num] if num in prefixSum else float('inf')
            # apply kadanes algo here
            prefixSum[num] = min(currentSum, currPrefixSum)
            currentSum+=num
        return maxSum if maxSum != float('-inf') else 0