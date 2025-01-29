class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        differenceArray = [0]*n
        for left, right in queries:
            differenceArray[left]+=1
            if right +1<n:
                differenceArray[right+1]-=1
        for i in range(1,n):
            differenceArray[i]+=differenceArray[i-1]
        
        for i in range(n):
            if nums[i] -differenceArray[i] >0:
                return False
        return True