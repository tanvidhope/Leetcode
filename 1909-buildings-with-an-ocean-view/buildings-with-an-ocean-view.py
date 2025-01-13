class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        maxHt = [-1]*n
        ans = []
        for i in range(n-2, -1, -1):
            maxHt[i] = max(maxHt[i+1], heights[i+1])
        for i in range(n):
            if maxHt[i] < heights[i]:
                ans.append(i)
        return ans