class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        sizeMap = defaultdict(int)
        k = 2
        n =len(grid)
        islandSize = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    size = self.dfs(grid, i,j, n, k)
                    sizeMap[k] = size
                    islandSize = max(islandSize, size)
                    k+=1
        #go through whites
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    left = self.getSize(grid, i, j-1, n)
                    right = self.getSize(grid, i, j+1, n)
                    up = self.getSize(grid, i-1, j, n)
                    down = self.getSize(grid, i+1, j, n)
                    currSize = 1
                    seen = set()
                    for color in (left, right, up, down):
                        if color not in seen:
                            seen.add(color)
                            currSize+=sizeMap[color]
                    islandSize = max(islandSize, currSize)
        return islandSize
        
    def dfs(self, grid, i, j, n, color):
        if i<0 or j<0 or i>=n or j>=n or grid[i][j]!=1:
            return 0
        count = 1
        grid[i][j] = color
        count+=self.dfs(grid, i+1, j, n, color)
        count+=self.dfs(grid, i, j+1, n, color)
        count+=self.dfs(grid, i-1, j, n, color)
        count+=self.dfs(grid, i, j-1, n, color)
        return count

    def getSize(self, grid, i, j, n):
        if i<0 or j<0 or i>=n or j>=n or grid[i][j] == 0:
            return 0
        return grid[i][j]
