class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxCount = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                maxCount = max(maxCount, self.dfs(matrix, i, j, m, n, memo))
        return maxCount+1

    def dfs(self, matrix, i, j, m, n, memo):
        neighbours = {(i+1, j), (i-1, j), (i, j+1), (i, j-1)}
        if (i,j) not in memo:
            maxCount = 0
            for newi, newj in neighbours:
                if 0<=newi<m and 0<=newj<n and matrix[newi][newj]>matrix[i][j]:
                    maxCount = max(maxCount, 1+self.dfs(matrix, newi, newj, m, n, memo))
            memo[(i,j)] = maxCount
        return memo[(i,j)]
