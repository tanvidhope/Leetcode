class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left<right:
            mid = left+(right-left)//2
            if self.canEat(piles, h, mid):
                right = mid
            else:
                left = mid+1
        return right

    def canEat(self, piles, h, k):
        currH = 0
        for pile in piles:
            currH+=pile//k
            currH +=1 if pile%k !=0 else 0
        return currH<=h