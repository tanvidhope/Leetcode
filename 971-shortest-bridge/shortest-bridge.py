class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        color = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i,j,n,n,color)
                    color+=1
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        neighbours = {(0,1), (1,0), (-1,0), (0,-1)}
        visited = set()
        while queue:
            i,j,dist = queue.popleft()
            for neighbour in neighbours:
                newi, newj = i+neighbour[0], j+neighbour[1]
                if 0<=newi<n and 0<=newj<n:
                    if grid[newi][newj] == 3:
                        return dist
                    elif (newi, newj) not in visited and grid[newi][newj] == 0:
                        visited.add((newi, newj))
                        queue.append((newi, newj, dist+1))
        return -1
        
    def dfs(self, grid, i, j, m, n, color):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0 or grid[i][j] == color:
            return
        grid[i][j] = color
        self.dfs(grid, i+1, j, m, n, color)
        self.dfs(grid, i-1, j, m, n, color)
        self.dfs(grid, i, j+1, m, n, color)
        self.dfs(grid, i, j-1, m, n, color)