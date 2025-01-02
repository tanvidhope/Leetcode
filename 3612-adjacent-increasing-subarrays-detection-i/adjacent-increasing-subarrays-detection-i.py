class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        hasSubarray = defaultdict(int)
        start, end = 0,1
        n = len(nums)
        if n // k < 2:
            return False
        if k == 1:
            return True
        while end < n:
            while end < n and nums[end] > nums[end - 1]:
                if end - start + 1 == k:
                    hasSubarray[start] = 1
                    start += 1
                end += 1
            start = end
            end += 1

        for key in hasSubarray:
            if (key+k) in hasSubarray:
                return True
        return False           