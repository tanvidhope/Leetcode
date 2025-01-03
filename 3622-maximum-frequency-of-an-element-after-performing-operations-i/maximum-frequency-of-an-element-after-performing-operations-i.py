class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        # binary search on the target value
        nums.sort()
        count = Counter(nums)

        def maxFreq(target):
            left = bisect_left(nums, target-k)
            right = bisect_left(nums, target+k+1)
            options = right-left-count[target] # subtract the count of elements which are already target
            return min(options, numOperations) + count[target]

        ans = 0
        for i in range(min(nums), max(nums)+1):
            ans = max(ans, maxFreq(i))
        return ans
        