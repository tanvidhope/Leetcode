class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #difference Array
        diff = [0]*len(nums)
        for query in queries:
            if query[0]<len(nums):
                diff[query[0]]+=1
            if query[1]+1<len(nums):
                diff[query[1]+1]-=1

        for i in range(len(nums)):
            diff[i]+=diff[i-1] if i>0 else 0
            if nums[i]-diff[i]>0:
                return False
        return True