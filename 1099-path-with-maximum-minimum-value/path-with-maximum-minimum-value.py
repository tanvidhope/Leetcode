class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # dijkstra
        rows, cols = len(grid), len(grid[0])
        directions = {(0,1), (1,0), (-1, 0), (0,-1)}
        pq = []
        ans = grid[0][0]
        visited = [[False]*cols for i in range(rows)]

        heapq.heappush(pq, (-grid[0][0], 0, 0))
        visited[0][0] = True
        while pq:
            val, row, col = heapq.heappop(pq)
            ans = min(ans, grid[row][col])
            if row ==rows-1 and col==cols-1:
                return ans
            for dRow, dCol in directions:
                newRow, newCol = row+dRow, col+dCol
                if 0<=newRow<rows and 0<=newCol<cols and not visited[newRow][newCol]:
                    heapq.heappush(pq, (-grid[newRow][newCol], newRow, newCol))
                    visited[newRow][newCol] = True
        return ans