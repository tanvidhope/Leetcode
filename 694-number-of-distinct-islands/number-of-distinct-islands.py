class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # subract row and col values by start row and col for translation

        uniqueIslands = []
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currentIsland = self.dfs(grid, i, j, m, n,[])
                    #translate the island
                    for x in range(len(currentIsland)):
                        currentIsland[x][0] = currentIsland[x][0]-i
                        currentIsland[x][1] = currentIsland[x][1]-j

                    # checkUnique
                    if self.isUniqueIsland(currentIsland, uniqueIslands):
                        uniqueIslands.append(currentIsland)
                    
        return len(uniqueIslands)

    
    def dfs(self, grid, i, j, m, n, ans):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
            return ans
        ans.append([i,j])
        grid[i][j] = 0
        ans = self.dfs(grid, i+1, j, m, n, ans)
        ans = self.dfs(grid, i-1, j, m, n, ans)
        ans = self.dfs(grid, i, j+1, m,n, ans)
        ans = self.dfs(grid, i, j-1, m, n, ans)
        return ans
    
    def isUniqueIsland(self, current, islandList):
        for island in islandList:
            if len(island)!= len(current):
                continue
            i = 0
            while i<len(island) and current[i][0] == island[i][0] and current[i][1] == island[i][1]:
                i+=1
            if i == len(island):
                return False
        return True