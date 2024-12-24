class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        currSum = 0
        count = 0
        for num in nums:
            currSum +=num
            if currSum-k in hmap:
                count+= hmap[currSum-k]
            hmap[currSum] += 1
        return count