class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        ans = [0]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] <heights[i]:
                stack.pop()
                ans[i]+=1
            ans[i]+= 1 if stack else 0
            stack.append(i)
        return ans