class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        startIndices, endIndices = [], []
        for query in queries:
            startIndices.append(query[0])
            endIndices.append(query[1])
        startIndices.sort()
        endIndices.sort()
        i, j = 0,0
        maxTransform = 0
        for x in range(len(nums)):
            while i<len(startIndices) and startIndices[i] == x:
                maxTransform+=1
                i+=1
            while j< len(endIndices) and endIndices[j] == x-1:
                maxTransform-=1
                j+=1
            nums[x] = max(nums[x]-maxTransform, 0)
        return sum(nums) == 0
