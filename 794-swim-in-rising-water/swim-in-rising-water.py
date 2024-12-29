class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # priority queue, keep track of max value 
        pq = []
        n = len(grid)
        if n==1 and len(grid[0])==1:
            return grid[0][0]
        neighbours=  {(0,1), (1,0), (-1, 0), (0, -1)}
        pq.append((grid[0][0],0,0))
        visited = set()
        while pq:
            wt, i,j = heapq.heappop(pq)
            for neighbour in neighbours:
                newi, newj = i+neighbour[0], j+neighbour[1]
                if newi==n-1 and newj==n-1:
                    return max(grid[newi][newj], wt)
                if 0<=newi<n and 0<=newj<n and (newi, newj) not in visited:
                    visited.add((newi, newj))
                    heapq.heappush(pq, (max(grid[newi][newj], wt),newi, newj))
        return -1
