class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        newNums = sorted(set(nums)) # this removes the duplicates
        j = 0
        for i in range(len(newNums)):
            while j < len(newNums) and newNums[j] < newNums[i]+n:
                j+=1
            count = j-i
            ans = min(ans, n-count)
        return ans