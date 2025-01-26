class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows1, cols1= len(grid), len(grid[0])
        rows2, cols2 = 3*rows1, 3*cols1
        grid2 = [[0]*cols2 for i in range(rows2)]

        for r in range(rows1):
            for c in range(cols1):
                r2, c2 = 3*r, 3*c
                if grid[r][c] == '/':
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                elif grid[r][c] == '\\':
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        
        visited = set()
        ans = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r,c) not in visited:
                    ans+=1
                    self.dfs(grid2, r, c, visited)
        return ans

    
    def dfs(self, grid, r,c, visited):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!=0:
            return
        neighbours = {(r + 1, c), (r, c +1), (r-1, c), (r, c-1)}
        for nr, nc in neighbours:
            if (nr, nc) not in visited:
                visited.add((nr,nc))
                self.dfs(grid, nr, nc, visited)
    
