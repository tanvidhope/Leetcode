class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # binary search
        left, right = 1, n*m
        while (left<right):
            mid = left+(right-left)//2
            if self.isEnough(m, n, mid, k):
                right = mid
            else:
                left = mid+1
        return left

    def isEnough(self, m, n, mid, k):
        count = 0
        for val in range(1, m+1):
            add = min(mid//val, n)
            if add == 0:
                break
            count+=add
        return count >=k