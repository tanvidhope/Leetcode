class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                # compute the max area with lower right corner at (i,j)
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxArea = max(maxArea, width*(i-k+1))
        return maxArea