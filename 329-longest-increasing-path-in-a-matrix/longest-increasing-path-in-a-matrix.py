class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix), len(matrix[0])
        maxLen = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                maxLen = max(maxLen, self.dfs(matrix, i,j,m,n, -1, memo))
        return maxLen
        
    def dfs(self, matrix, i,j, m,n, prev, memo):
        if i<0 or j<0 or i>=m or j>=n or matrix[i][j] <=prev:
            return 0
        if (i,j) not in memo:
            maxLen = 0
            neighbours={(i+1, j), (i, j+1), (i-1, j), (i, j-1)}
            for newi, newj in neighbours:
                maxLen = max(maxLen, self.dfs(matrix, newi, newj, m, n, matrix[i][j], memo))
            memo[(i,j)] = 1+maxLen
        return memo[(i,j)]